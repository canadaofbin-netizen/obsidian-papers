import os

wiki_dir = r"G:\My Drive\UCL\AI Lab\obsidian practice\wiki"
papers = [
    "Paper - Calderwood 2023.md",
    "Paper - Dalal 2020.md",
    "Paper - Judge 2015.md",
    "Paper - Meyer 2009.md"
]

all_concepts = [
    "[[Active Inference and Generative Priors in Workplaces]]",
    "[[Organizational Thermodynamics and Behavioral Entropy]]",
    "[[The Free Energy Paradigm of Organizational Control]]"
]

for p in papers:
    p_path = os.path.join(wiki_dir, p)
    with open(p_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    missing_concepts = []
    for c in all_concepts:
        if c not in content:
            missing_concepts.append(c)
    
    if missing_concepts:
        with open(p_path, "a", encoding="utf-8") as f:
            for c in missing_concepts:
                f.write(f"* {c}\n")
        print(f"Appended to {p}: {missing_concepts}")
    else:
        print(f"No missing concepts for {p}")
