from pyformlang.finite_automaton import DeterministicFiniteAutomaton

def create_nombre_dfa():
    nombre_dfa = DeterministicFiniteAutomaton()
    nombre_dfa.add_start_state("q0")
    nombre_dfa.add_final_state("q1")
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        nombre_dfa.add_transition("q0", letter, "q1")
        nombre_dfa.add_transition("q1", letter, "q1")
    return nombre_dfa

def create_telefono_dfa():
    telefono_dfa = DeterministicFiniteAutomaton()
    telefono_dfa.add_start_state("q0")
    telefono_dfa.add_final_state("q9")
    for i in range(10):  # Dígitos del 0 al 9
        telefono_dfa.add_transition("q0", str(i), "q1")
        telefono_dfa.add_transition("q1", str(i), "q2")
        telefono_dfa.add_transition("q2", str(i), "q3")
        telefono_dfa.add_transition("q3", str(i), "q4")
        telefono_dfa.add_transition("q4", str(i), "q5")
        telefono_dfa.add_transition("q5", str(i), "q6")
        telefono_dfa.add_transition("q6", str(i), "q7")
        telefono_dfa.add_transition("q7", str(i), "q8")
    telefono_dfa.add_transition("q8", "-", "q9")
    return telefono_dfa

def create_identificacion_dfa():
    identificacion_dfa = DeterministicFiniteAutomaton()
    identificacion_dfa.add_start_state("q0")
    identificacion_dfa.add_final_state("q10")
    for i in range(10):  # Dígitos del 0 al 9
        identificacion_dfa.add_transition("q0", str(i), "q1")
        identificacion_dfa.add_transition("q1", str(i), "q2")
        identificacion_dfa.add_transition("q2", str(i), "q3")
        identificacion_dfa.add_transition("q3", str(i), "q4")
        identificacion_dfa.add_transition("q4", str(i), "q5")
        identificacion_dfa.add_transition("q5", str(i), "q6")
        identificacion_dfa.add_transition("q6", str(i), "q7")
        identificacion_dfa.add_transition("q7", str(i), "q8")
        identificacion_dfa.add_transition("q8", str(i), "q9")
        identificacion_dfa.add_transition("q9", str(i), "q10")  
    return identificacion_dfa
