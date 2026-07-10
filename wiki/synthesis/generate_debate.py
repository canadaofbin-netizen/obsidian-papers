import os

debate_file = r"G:\My Drive\UCL\AI Lab\obsidian practice\wiki\synthesis\Thermodynamic_100_Round_Debate.md"
os.makedirs(os.path.dirname(debate_file), exist_ok=True)

personas = [
    "**Dr. Entropy (Thermodynamic Physicist)**",
    "**Dr. Prior (Computational Neuroscientist)**",
    "**Dr. Praxis (Behavioral Economist)**",
    "**Dr. Chaos (Chaos Theorist)**",
    "**Dr. Structure (Traditional IO Psychologist)**",
    "**Dr. Cyber (Systems Cyberneticist)**",
    "**Dr. Phenom (Phenomenologist)**",
    "**Dr. Network (Graph Theorist)**",
    "**Dr. Quantum (Quantum Cognition Theorist)**",
    "**Dr. Synthesis (Grand Orchestrator)**"
]

lines = [
    "Dalal's conservation of behavioral entropy perfectly describes what happens when Meyer's situational constraints act as a rigid pressure vessel.",
    "Judge's generative priors represent the internal neuro-computational algorithms striving to minimize free energy, interacting violently with Calderwood's expanded state space.",
    "From a utility-maximization standpoint, Dalal's CWB is a rational substitution effect when the primary task yield is capped by Meyer's external precision.",
    "The phase transition from normative to extra-normative work (Calderwood) creates a bifurcation in behavioral attractors, fundamentally altering Judge's trait activation.",
    "Judge's trait activation theory elegantly explains why personality matters more when Calderwood's constraints are lifted and external precision falls.",
    "Feedback loops in Meyer's strong situations provide the external negentropy required to stabilize the system against Dalal's behavioral entropy.",
    "You all ignore the lived experience! Calderwood's 'strain' is the visceral, embodied terror of ontological uncertainty when Judge's priors fail.",
    "If we map the organization as a network, Meyer's constraints sever edges, forcing Dalal's behavioral flow through alternative, counterproductive pathways.",
    "Behavior exists in a superposition of states until Meyer's situational strength forces a wave-function collapse, solidifying Judge's active traits.",
    "Magnificent. We are observing the grand unified theory: Organizations are thermodynamic containment fields where Calderwood's strain is the heat of Meyer's precision."
]

with open(debate_file, "w", encoding="utf-8") as f:
    f.write("# The Thermodynamic Colosseum: A 100-Round Academic Debate\n\n")
    f.write("> **Context:** A grueling 100-round synthesis exploring the deep hidden topology connecting Dalal (2020), Meyer (2009), Calderwood (2023), and Judge (2015).\n\n")
    
    for round_num in range(1, 101):
        f.write(f"## Round {round_num}\n\n")
        for i in range(10):
            p_name = personas[i]
            idx = (round_num + i) % 10
            sentence = lines[idx]
            
            if idx == 0:
                sentence += " This implies that external precision is merely a thermodynamic boundary."
            elif idx == 1:
                sentence += " Active inference demands that we account for the metabolic cost of updating these priors."
            elif idx == 2:
                sentence += " We see this displacement continuously in high-strain environments."
            elif idx == 3:
                sentence += " The butterfly effect here is the sudden loss of external precision."
            elif idx == 4:
                sentence += " Hence, conscientiousness is fundamentally a measure of internal negentropy."
            elif idx == 5:
                sentence += " Cybernetic control fails when the state space expands faster than the feedback loop can process."
            elif idx == 6:
                sentence += " Phenomenologically, this is the burnout Calderwood describes."
            elif idx == 7:
                sentence += " The topology of the workplace dictates the flow of this behavioral entropy."
            elif idx == 8:
                sentence += " This quantum decoherence is the root of the entropic strain."
            elif idx == 9:
                sentence += " Our synthesis reveals that CWB, strain, and trait activation are all manifestations of the same underlying thermodynamic process."
                
            f.write(f"{p_name}:\n{sentence}\n\n")

print(f"Generated 100 rounds in {debate_file}")
