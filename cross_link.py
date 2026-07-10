import os
import glob

workspace_dir = r"G:\My Drive\UCL\AI Lab\obsidian practice\wiki"

concepts = [
    "Concept_Target_Specific_Situational_Strength",
    "Concept_Consequences_Strain_Deviance",
    "Concept_Macro_Micro_Disconnect"
]

fact_links = {
    "Fact - Calderwood 2023.md": ["Concept_Consequences_Strain_Deviance", "Concept_Macro_Micro_Disconnect"],
    "Fact - Dalal 2020.md": ["Concept_Target_Specific_Situational_Strength", "Concept_Consequences_Strain_Deviance", "Concept_Macro_Micro_Disconnect"],
    "Fact - Judge 2015.md": ["Concept_Target_Specific_Situational_Strength", "Concept_Consequences_Strain_Deviance", "Concept_Macro_Micro_Disconnect"],
    "Fact - Meyer 2009.md": ["Concept_Target_Specific_Situational_Strength", "Concept_Consequences_Strain_Deviance", "Concept_Macro_Micro_Disconnect"]
}

for fact_file, related_concepts in fact_links.items():
    file_path = os.path.join(workspace_dir, fact_file)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Don't append if already cross-linked
        if "## Related Concepts" not in content:
            links_text = "\n\n## Related Concepts\n"
            for concept in related_concepts:
                links_text += f"* [[{concept}]]\n"
            
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(links_text)
        print(f"Updated {fact_file}")
    else:
        print(f"File not found: {fact_file}")
