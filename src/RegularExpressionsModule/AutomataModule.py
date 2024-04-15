import re
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex


name_regularPhrase = r'[A-Za-z]+\s[A-Za-z]+'
date_regularPhrase = r'\d{2}/\d{2}/\d{4}'
direction_regularPhrase = r'\d+\s[A-Za-z]+\s[A-Za-z]+'
phone_regularPhrase = r'\d{3}-\d{3}-\d{4}'
email_regularPhrase = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
identification_regularPhrase = r'[A-Z0-9]{8}'


def create_nombre_dfa():
    nombre_dfa = DeterministicFiniteAutomaton()
    nombre_dfa.add_start_state("q0")
    nombre_dfa.add_final_state("q1")
    nombre_dfa.add_transition("q0", " ", "q1")
    nombre_dfa.add_transition("q1", " ", "q1")
    nombre_dfa.add_transition("q1", "a", "q1")
    nombre_dfa.add_transition("q1", "b", "q1")
    return nombre_dfa

def create_fecha_nfa():
    fecha_regex_str = "(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}"
    fecha_regex = Regex(fecha_regex_str)
    fecha_nfa = fecha_regex.to_epsilon_nfa().minimize()
    return fecha_nfa

def create_direccion_dfa():
    direccion_dfa = DeterministicFiniteAutomaton()
    direccion_dfa.add_start_state("q0")
    direccion_dfa.add_final_state("q1")
    direccion_dfa.add_transition("q0", " ", "q1")
    direccion_dfa.add_transition("q1", " ", "q1")
    direccion_dfa.add_transition("q1", "123", "q1")  
    return direccion_dfa

def create_telefono_dfa():
    telefono_dfa = DeterministicFiniteAutomaton()
    telefono_dfa.add_start_state("q0")
    telefono_dfa.add_final_state("q9")
    for i in range(10):
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

def create_email_dfa():
    email_dfa = DeterministicFiniteAutomaton()
    email_dfa.add_start_state("q0")
    email_dfa.add_final_state("q4")
    email_dfa.add_transition("q0", "@", "q1")
    email_dfa.add_transition("q1", ".", "q2")
    email_dfa.add_transition("q2", "com", "q3")
    email_dfa.add_transition("q3", "", "q4")
    return email_dfa

def create_identificacion_dfa():
    identificacion_dfa = DeterministicFiniteAutomaton()
    identificacion_dfa.add_start_state("q0")
    identificacion_dfa.add_final_state("q7")
    for i in range(10):
        identificacion_dfa.add_transition("q0", str(i), "q1")
        identificacion_dfa.add_transition("q1", str(i), "q2")
        identificacion_dfa.add_transition("q2", str(i), "q3")
        identificacion_dfa.add_transition("q3", str(i), "q4")
        identificacion_dfa.add_transition("q4", str(i), "q5")
        identificacion_dfa.add_transition("q5", str(i), "q6")
    identificacion_dfa.add_transition("q6", str(i), "q7")
    return identificacion_dfa

