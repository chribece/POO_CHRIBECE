from abc import ABC, abstractmethod
# Abstracción: Clase madre abstracta

class cuentabancaria(ABC):
    def __init__(self, titular, saldo):
        self._titular = titular # Encapsulación: atributo protegido
        self._saldo = saldo # Encapsulación: atributo protegido

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def retirar(self, monto):
        pass

    def mostrar_informacion(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}"

# Herencia y Polimorfismo: Subclases específicas

# Subclase1: Cuenta Ahorro
class cuentaahorros(cuentabancaria):
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito realizado. Nuevo saldo: {self._saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro realizado. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

# Subclase2: Cuenta Corriente
class cuentacorriente(cuentabancaria):
    def __init__(self, titular, saldo, credito):
        super().__init__(titular, saldo)
        self._credito = credito # Atributo específico de cuenta corriente

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito realizado. Nuevo saldo: {self._saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self._saldo + self._credito:
            self._saldo -= monto
            print(f"Retiro realizado. Nuevo saldo: {self._saldo}")
        else:
            print("Excede el límite de descubierto o monto inválido.")

# Ejecución
def main():
    cuenta_ahorros = cuentaahorros("Juan Pérez", 5000)
    cuenta_corriente = cuentacorriente("María López", 2000, 1000)

    print(cuenta_ahorros.mostrar_informacion())
    cuenta_ahorros.depositar(1500)
    cuenta_ahorros.retirar(3000)

    print(cuenta_corriente.mostrar_informacion())
    cuenta_corriente.depositar(500)
    cuenta_corriente.retirar(3200)

if __name__ == "__main__":
    main()
