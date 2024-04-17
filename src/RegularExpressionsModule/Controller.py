from . import AutomataModule, RegularExpression
import re

class Controller:
    def __init__(self):
        self.is_valid_name = ''
        self.is_valid_phone = ''
        self.is_valid_id = ''

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
        maches_name = re.findall(RegularExpression.name_regularPhrase, input_string)
        if maches_name:
            for mach in maches_name:
                print(mach)
                self.is_valid_name = self._validate_nombre(mach)
                print(self.is_valid_name)

        # Validar teléfono
        maches_phone = re.findall(RegularExpression.phone_regularPhrase, input_string)
        if maches_phone:
            for mach in maches_phone:
                is_valid_phone = self._validate_telefono(mach)

        # Validar identificación
        maches_id = re.findall(RegularExpression.identification_name_regularPhrase, input_string)
        if maches_id:
            for mach in maches_id:
                is_valid_id = self._validate_identificacion(input_string)

        return {
            "is_valid_name": self.is_valid_name,
            "is_valid_phone": self.is_valid_phone,
            "is_valid_id": self.is_valid_id
        }
