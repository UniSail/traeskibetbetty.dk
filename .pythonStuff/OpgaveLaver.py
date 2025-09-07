import re
from collections import defaultdict

def extract_tasks_from_markdown(file_path):
    """
    Extract tasks for each person from the markdown meeting notes
    """
    # Dictionary to store tasks for each person
    person_tasks = defaultdict(list)
    
    # People we're looking for
    target_people = ['Morten', 'Jens', 'Jeppe', 'Frederik', 'Malene', 'Magnus', 'Jakob', 'Hans', 'Amanda']
    
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
            
            # Look for task lines (lines with [ ])
            if '- [ ]' in line:
                # Extract the task text
                task_text = line.strip()
                
                # Look for person names in the current line
                for person in target_people:
                    if person in line:
                        # Clean up the task text
                        clean_task = re.sub(r'- \[ \]', '', task_text).strip()
                        person_tasks[person].append({
                            'task': clean_task,
                            'section': current_section,
                            'line_number': i + 1
                        })
                
                # Also check the next few lines for person assignments
                for j in range(1, 4):  # Check next 3 lines
                    if i + j < len(lines):
                        next_line = lines[i + j]
                        if next_line.strip().startswith('-') or next_line.strip() == '':
                            break  # Stop if we hit another task or empty line
                        
                        for person in target_people:
                            if person in next_line:
                                clean_task = re.sub(r'- \[ \]', '', task_text).strip()
                                person_tasks[person].append({
                                    'task': clean_task,
                                    'section': current_section,
                                    'line_number': i + 1,
                                    'context': next_line.strip()
                                })
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    return person_tasks

def generate_person_task_list(person, tasks):
    """
    Generate a formatted task list for a specific person
    """
    if not tasks:
        return f"Ingen opgaver fundet for {person} 🎉"
    
    output = f"""
📋 **Opgaveliste for {person}**
{'=' * (20 + len(person))}

Du har {len(tasks)} opgave{'r' if len(tasks) > 1 else ''} fra bestyrelsesmødet:

"""
    
    # Group tasks by section
    sections = defaultdict(list)
    for task in tasks:
        sections[task['section']].append(task)
    
    for section, section_tasks in sections.items():
        if section:
            output += f"## {section}\n\n"
        
        for i, task in enumerate(section_tasks, 1):
            output += f"{i}. {task['task']}\n"
            if 'context' in task:
                output += f"   💡 {task['context']}\n"
            output += "\n"
    
    output += "Har du spørgsmål til opgaverne, så skriv endelig! 😊\n"
    return output

def main():
    # Path to the markdown file
    md_file_path = r"c:\Users\Jeppe\Programmering\Programmering\traeskibetbetty.dk\content\Posts\Nyheder\2025-09.md"
    
    # Extract tasks
    print("Udvinder opgaver fra bestyrelsesmøde...")
    person_tasks = extract_tasks_from_markdown(md_file_path)
    
    # Generate individual task lists
    target_people = ['Morten', 'Jens', 'Jeppe', 'Frederik', 'Malene']
    
    for person in target_people:
        tasks = person_tasks.get(person, [])
        task_list = generate_person_task_list(person, tasks)
        
        # Save to individual files
        output_file = f".pythonStuff/{person}_opgaver.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(task_list)
            print(f"✅ Opgaveliste for {person} gemt som {output_file}")
        except Exception as e:
            print(f"❌ Fejl ved gemning af fil for {person}: {e}")
        
        # Also print to console
        print(f"\n{task_list}")
        print("-" * 50)
    
    # Print summary
    print(f"\n📊 **Sammenfatning:**")
    for person in target_people:
        count = len(person_tasks.get(person, []))
        print(f"{person}: {count} opgave{'r' if count != 1 else ''}")

if __name__ == "__main__":
    main()