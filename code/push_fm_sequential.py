import os, subprocess, sys

base_dir = "financial_modelling"
sessions = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])

print(f"Found {len(sessions)} sessions in {base_dir}")

for idx, session in enumerate(sessions, 1):
    session_path = os.path.join(base_dir, session)
    print(f"\n[{idx}/{len(sessions)}] Processing {session}...")
    
    # 1. git add
    res_add = subprocess.run(["git", "add", session_path], capture_output=True, text=True)
    if res_add.returncode != 0:
        print(f"Error git add: {res_add.stderr}")
        sys.exit(1)
        
    # Check if there are changes to commit
    diff_check = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    if not diff_check.stdout.strip():
        print(f"Nothing staged for {session}, skipping commit/push.")
        continue
        
    # 2. git commit
    # Extract clean title from README
    readme_path = os.path.join(session_path, "README.md")
    commit_desc = session.replace("_", " ")
    if os.path.exists(readme_path):
        with open(readme_path) as f:
            first_line = f.readline().strip()
            if first_line.startswith("# "):
                commit_desc = first_line.replace("# ", "")
                
    commit_msg = f"feat(financial_modelling): add {session} - {commit_desc}"
    res_commit = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
    if res_commit.returncode != 0:
        print(f"Error git commit: {res_commit.stderr}")
        sys.exit(1)
        
    # 3. git push
    print(f"Pushing commit for {session} to origin main...")
    res_push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    if res_push.returncode != 0:
        print(f"Error git push: {res_push.stderr}")
        sys.exit(1)
    print(f"Successfully pushed {session}!")

print("\nAll financial modelling sessions have been committed and pushed sequentially!")
