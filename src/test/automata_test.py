import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RegularExpressionsModule.AutomataModule import create_nombre_dfa, create_telefono_dfa, create_identificacion_dfa

class automata_test(unittest.TestCase):
    def test_create_nombre_dfa(self):
        nombre_dfa = create_nombre_dfa()
        self.assertIn("q0", nombre_dfa.states)
        self.assertIn("q1", nombre_dfa.states)
        self.assertEqual(nombre_dfa.start_state, "q0")
        self.assertIn("q1", nombre_dfa.final_states)
        for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertIn(("q0", letter, "q1"), nombre_dfa.transitions)
            self.assertIn(("q1", letter, "q1"), nombre_dfa.transitions)

    def test_create_telefono_dfa(self):
        telefono_dfa = create_telefono_dfa()
        self.assertIn("q0", telefono_dfa.states)
        self.assertIn("q9", telefono_dfa.states)
        self.assertEqual(telefono_dfa.start_state, "q0")
        self.assertIn("q9", telefono_dfa.final_states)
        for i in range(10):
            self.assertIn(("q0", str(i), "q1"), telefono_dfa.transitions)
            self.assertIn(("q1", str(i), "q2"), telefono_dfa.transitions)
            self.assertIn(("q2", str(i), "q3"), telefono_dfa.transitions)
            self.assertIn(("q3", str(i), "q4"), telefono_dfa.transitions)
            self.assertIn(("q4", str(i), "q5"), telefono_dfa.transitions)
            self.assertIn(("q5", str(i), "q6"), telefono_dfa.transitions)
            self.assertIn(("q6", str(i), "q7"), telefono_dfa.transitions)
            self.assertIn(("q7", str(i), "q8"), telefono_dfa.transitions)
        self.assertIn(("q8", "-", "q9"), telefono_dfa.transitions)

    def test_create_identificacion_dfa(self):
        identificacion_dfa = create_identificacion_dfa()
        self.assertIn("q0", identificacion_dfa.states)
        self.assertIn("q10", identificacion_dfa.states)
        self.assertEqual(identificacion_dfa.start_state, "q0")
        self.assertIn("q10", identificacion_dfa.final_states)
        for i in range(10):
            self.assertIn(("q0", str(i), "q1"), identificacion_dfa.transitions)
            self.assertIn(("q1", str(i), "q2"), identificacion_dfa.transitions)
            self.assertIn(("q2", str(i), "q3"), identificacion_dfa.transitions)
            self.assertIn(("q3", str(i), "q4"), identificacion_dfa.transitions)
            self.assertIn(("q4", str(i), "q5"), identificacion_dfa.transitions)
            self.assertIn(("q5", str(i), "q6"), identificacion_dfa.transitions)
            self.assertIn(("q6", str(i), "q7"), identificacion_dfa.transitions)
            self.assertIn(("q7", str(i), "q8"), identificacion_dfa.transitions)
            self.assertIn(("q8", str(i), "q9"), identificacion_dfa.transitions)
            self.assertIn(("q9", str(i), "q10"), identificacion_dfa.transitions)
if __name__ == '__main__':
    unittest.main()
