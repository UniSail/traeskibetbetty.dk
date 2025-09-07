import re
from collections import defaultdict
import os
from datetime import datetime

def extract_tasks_from_markdown(file_path):
    """
    Extract tasks for each person from the markdown meeting notes
    """
    # Dictionary to store tasks for each person
    person_tasks = defaultdict(lambda: {'pending': [], 'completed': []})
    
    # People we're looking for
    target_people = ['Morten', 'Jens', 'Jeppe', 'Frederik', 'Malene', 'Magnus', 'Jakob', 'Hans', 'Amanda', 'Tommy', 'Mads', 'Kat', 'Bo', 'Ida']    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split into lines for processing
        lines = content.split('\n')
        current_section = ""
        
        for i, line in enumerate(lines):
            # Track current section for context
            if line.startswith('#'):
                current_section = line.strip('#').strip()
            
            # Look for task lines (both pending and completed)
            if re.search(r'- \[([ x])\]', line):
                # Extract the task text and status
                task_match = re.search(r'- \[([ x])\](.+)', line)
                if task_match:
                    is_completed = task_match.group(1) == 'x'
                    task_text = task_match.group(2).strip()
                    
                    # Look for person names in the current line
                    for person in target_people:
                        if person in line:
                            task_data = {
                                'task': task_text,
                                'section': current_section,
                                'line_number': i + 1,
                                'original_line': line.strip()
                            }
                            
                            if is_completed:
                                person_tasks[person]['completed'].append(task_data)
                            else:
                                person_tasks[person]['pending'].append(task_data)
                    
                    # Also check the next few lines for person assignments
                    for j in range(1, 4):  # Check next 3 lines
                        if i + j < len(lines):
                            next_line = lines[i + j]
                            if next_line.strip().startswith('-') or next_line.strip() == '':
                                break  # Stop if we hit another task or empty line
                            
                            for person in target_people:
                                if person in next_line:
                                    task_data = {
                                        'task': task_text,
                                        'section': current_section,
                                        'line_number': i + 1,
                                        'context': next_line.strip(),
                                        'original_line': line.strip()
                                    }
                                    
                                    if is_completed:
                                        person_tasks[person]['completed'].append(task_data)
                                    else:
                                        person_tasks[person]['pending'].append(task_data)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    return person_tasks

def generate_person_markdown(person, person_data):
    """
    Generate a markdown file for a specific person
    """
    pending_tasks = person_data['pending']
    completed_tasks = person_data['completed']
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Generate front matter
    output = f"""---
date: {current_date}
draft: false
title: "Opgaveliste for {person} - September 2025"
ShowToc: true
TocOpen: true
hidden: false
tags: ["opgaver", "{person.lower()}", "bestyrelsesmøde"]
---

# 📋 Opgaveliste for {person}

*Genereret fra bestyrelsesmøde d. 3. September 2025*

"""

    # Pending tasks section
    if pending_tasks:
        output += f"""## 🎯 Aktuelle opgaver ({len(pending_tasks)} stk.)

"""
        # Group pending tasks by section
        sections = defaultdict(list)
        for task in pending_tasks:
            sections[task['section']].append(task)
        
        for section, section_tasks in sections.items():
            if section:
                output += f"### {section}\n\n"
            
            for i, task in enumerate(section_tasks, 1):
                output += f"- [ ] **{task['task']}**\n"
                if 'context' in task:
                    output += f"  - *Detaljer: {task['context']}*\n"
                output += "\n"
    else:
        output += "## 🎯 Aktuelle opgaver\n\n🎉 **Ingen aktuelle opgaver!** Du er opdateret! 🎉\n\n"

    # Completed tasks section
    if completed_tasks:
        output += f"""## ✅ Gennemførte opgaver ({len(completed_tasks)} stk.)

*Godt arbejde! Her er de opgaver du allerede har løst:*

"""
        # Group completed tasks by section
        sections = defaultdict(list)
        for task in completed_tasks:
            sections[task['section']].append(task)
        
        for section, section_tasks in sections.items():
            if section:
                output += f"### {section}\n\n"
            
            for task in section_tasks:
                output += f"- [x] ~~{task['task']}~~ ✨\n"
                if 'context' in task:
                    output += f"  - *{task['context']}*\n"
                output += "\n"
    else:
        output += "## ✅ Gennemførte opgaver\n\n*Ingen registrerede gennemførte opgaver endnu.*\n\n"

    # Footer
    output += f"""---

💡 **Har du spørgsmål til opgaverne?** Skriv endelig til bestyrelsen!

� **Fandt du en fejl?** Kontakt Jeppe så listen kan blive opdateret.

*Sidst opdateret: {current_date}*
"""

    return output

def main():
    # Path to the Nyheder folder
    nyheder_dir = r"content\Posts\Nyheder"

    # Output directory
    output_dir = r"content\Posts\Nyheder\Opgavelisten"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Find all markdown files in Nyheder folder
    markdown_files = [f for f in os.listdir(nyheder_dir) if f.endswith('.md')]

    # Extract tasks from all files
    print(f"🔍 Udvinder opgaver fra {len(markdown_files)} markdown filer...")
    person_tasks = defaultdict(lambda: {'pending': [], 'completed': []})

    for md_file in markdown_files:
        md_file_path = os.path.join(nyheder_dir, md_file)
        print(f"   📄 Behandler: {md_file}")
        file_tasks = extract_tasks_from_markdown(md_file_path)
        
        # Merge tasks from this file with the overall collection
        for person, tasks in file_tasks.items():
            person_tasks[person]['pending'].extend(tasks['pending'])
            person_tasks[person]['completed'].extend(tasks['completed'])
        
        # Generate individual task lists
        target_people = ['Morten', 'Jens', 'Jeppe', 'Frederik', 'Malene']
        
        for person in target_people:
            person_data = person_tasks.get(person, {'pending': [], 'completed': []})
            markdown_content = generate_person_markdown(person, person_data)
            
            # Save to markdown files
            output_file = os.path.join(output_dir, f"{person}-opgaver.md")
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(markdown_content)
                print(f"✅ Opgaveliste for {person} gemt som {output_file}")
            except Exception as e:
                print(f"❌ Fejl ved gemning af fil for {person}: {e}")
            
            # Print summary to console
            pending_count = len(person_data['pending'])
            completed_count = len(person_data['completed'])
            print(f"📊 {person}: {pending_count} aktive opgaver, {completed_count} gennemførte")
            
            if completed_count > 0:
                print(f"   🎉 Tillykke med de gennemførte opgaver!")
        
        # Print overall summary
        print(f"\n� **Samlet oversigt:**")
        total_pending = 0
        total_completed = 0
        
        for person in target_people:
            person_data = person_tasks.get(person, {'pending': [], 'completed': []})
            pending = len(person_data['pending'])
            completed = len(person_data['completed'])
            total_pending += pending
            total_completed += completed
            
            status = "🎯" if pending > 0 else "✨"
            print(f"{status} {person}: {pending} aktive, {completed} gennemførte")
        
        print(f"\n🚀 Total: {total_pending} aktive opgaver, {total_completed} gennemførte opgaver")
        print(f"📁 Markdown filer gemt i: {output_dir}")

if __name__ == "__main__":
    main()