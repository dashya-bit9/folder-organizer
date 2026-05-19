import os
import shutil
from groq import Groq

def scan_folder(folder_path):
    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            files.append(item)
    return files

def get_ai_organization_plan(files, groq_key):
    client = Groq(api_key=groq_key)
    
    files_list = "\n".join(files)
    
    prompt = f"""You are a file organization assistant.
    
    I have these files in a messy folder:
    {files_list}
    
    Create an organization plan. For each file suggest:
    1. Which subfolder it should go into
    2. A cleaner filename if the current one is messy
    
    Respond ONLY in this exact format, nothing else:
    filename.ext|New Folder Name|new_filename.ext
    
    One file per line. Every single file must be included."""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    
    return response.choices[0].message.content

def parse_plan(plan_text):
    moves = []
    lines = plan_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if "|" in line:
            parts = line.split("|")
            if len(parts) == 3:
                original, folder, new_name = parts
                moves.append({
                    "original": original.strip(),
                    "folder": folder.strip(),
                    "new_name": new_name.strip()
                })
    return moves

def execute_plan(folder_path, moves):
    results = []
    actual_files = os.listdir(folder_path)

    for move in moves:
        try:
            # Find the actual file even if name doesn't match exactly
            original_path = os.path.join(folder_path, move["original"])
            
            # If exact match doesn't exist try to find closest match
            if not os.path.exists(original_path):
                closest = None
                for actual_file in actual_files:
                    if actual_file.lower().replace(".", "_") == move["original"].lower().replace(".", "_"):
                        closest = actual_file
                        break
                if closest:
                    original_path = os.path.join(folder_path, closest)
                else:
                    results.append(f"❌ {move['original']} → Could not find file")
                    continue
            
            new_folder_path = os.path.join(folder_path, move["folder"])
            os.makedirs(new_folder_path, exist_ok=True)
            
            new_file_path = os.path.join(new_folder_path, move["new_name"])
            shutil.move(original_path, new_file_path)
            
            results.append(f"✅ {move['original']} → {move['folder']}/{move['new_name']}")
        except Exception as e:
            results.append(f"❌ {move['original']} → Error: {str(e)}")
    
    return results
    
