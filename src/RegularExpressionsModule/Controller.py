from . import AutomataModule

class Controller:
    def __init__(self):
        pass

    def _validate_nombre(self, input_string):
        dfa_nombre = AutomataModule.create_nombre_dfa()
        return dfa_nombre.accepts(input_string.strip())

    def _validate_telefono(self, input_string):
        dfa_telefono = AutomataModule.create_telefono_dfa()
        return dfa_telefono.accepts(input_string.strip())

    def _validate_identificacion(self, input_string):
        dfa_identificacion = AutomataModule.create_identificacion_dfa()
        return dfa_identificacion.accepts(input_string.strip())

    def validate_input(self, input_string):
        # Validar nombre
        is_valid_name = self._validate_nombre(input_string)

        # Validar teléfono
        is_valid_phone = self._validate_telefono(input_string)

        # Validar identificación
        is_valid_id = self._validate_identificacion(input_string)

        return {
            "is_valid_name": is_valid_name,
            "is_valid_phone": is_valid_phone,
            "is_valid_id": is_valid_id
        }
