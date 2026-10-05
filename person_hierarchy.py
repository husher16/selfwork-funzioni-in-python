from abc import ABC, abstractmethod


# ==========================================
# 1. Classe Astratta: Person
# ==========================================
class Person(ABC):
    """
    Classe base astratta che rappresenta una persona generica.
    Non può essere istanziata direttamente in quanto definisce il metodo astratto descrizione().
    """
    def __init__(self, nome: str, cognome: str, eta: int, email: str):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.email = email

    @abstractmethod
    def descrizione(self) -> str:
        """Metodo astratto: ogni sottoclasse concreta deve implementare la propria descrizione."""
        pass

    def saluta(self) -> str:
        """Metodo concreto comune a tutte le persone."""
        return f"Ciao, mi chiamo {self.nome} {self.cognome}."


# ==========================================
# 2. Sottoclasse: Studente (estende Person)
# ==========================================
class Studente(Person):
    """
    Sottoclasse di Person.
    Proprietà specializzanti: matricola, corso_di_laurea, voti (e calcolo media).
    """
    def __init__(self, nome: str, cognome: str, eta: int, email: str, matricola: str, corso_di_laurea: str):
        super().__init__(nome, cognome, eta, email)
        self.matricola = matricola
        self.corso_di_laurea = corso_di_laurea
        self.voti: list[float] = []

    def aggiungi_voto(self, voto: float):
        if 18 <= voto <= 30:
            self.voti.append(voto)
        else:
            raise ValueError("Il voto deve essere compreso tra 18 e 30.")

    @property
    def media_voti(self) -> float:
        return sum(self.voti) / len(self.voti) if self.voti else 0.0

    def descrizione(self) -> str:
        return (
            f"Studente: {self.nome} {self.cognome} (Matricola: {self.matricola}) | "
            f"Corso: {self.corso_di_laurea} | Media voti: {self.media_voti:.2f}"
        )


# ==========================================
# 3. Sottoclasse: Dipendente (estende Person)
# ==========================================
class Dipendente(Person):
    """
    Sottoclasse di Person.
    Proprietà specializzanti: id_dipendente, data_assunzione.
    Introduce anche il metodo astratto calcola_compenso_mensile().
    """
    def __init__(self, nome: str, cognome: str, eta: int, email: str, id_dipendente: str, data_assunzione: str):
        super().__init__(nome, cognome, eta, email)
        self.id_dipendente = id_dipendente
        self.data_assunzione = data_assunzione

    @abstractmethod
    def calcola_compenso_mensile(self) -> float:
        """Metodo astratto per il calcolo del compenso economico mensile."""
        pass

    def descrizione(self) -> str:
        return (
            f"Dipendente ID: {self.id_dipendente} - {self.nome} {self.cognome} "
            f"(Assunto il: {self.data_assunzione})"
        )


# ==========================================
# 4. Sottoclasse: Docente (estende Dipendente)
# ==========================================
class Docente(Dipendente):
    """
    Sottoclasse di Dipendente specializzata per docenti/insegnanti.
    Proprietà specializzanti: materia_insegnata, stipendio_base, ore_straordinario, tariffa_straordinario.
    """
    def __init__(
        self,
        nome: str,
        cognome: str,
        eta: int,
        email: str,
        id_dipendente: str,
        data_assunzione: str,
        materia_insegnata: str,
        stipendio_base: float,
        tariffa_straordinario: float = 30.0
    ):
        super().__init__(nome, cognome, eta, email, id_dipendente, data_assunzione)
        self.materia_insegnata = materia_insegnata
        self.stipendio_base = stipendio_base
        self.tariffa_straordinario = tariffa_straordinario
        self.ore_straordinario = 0

    def registra_straordinario(self, ore: int):
        self.ore_straordinario += ore

    def calcola_compenso_mensile(self) -> float:
        return self.stipendio_base + (self.ore_straordinario * self.tariffa_straordinario)

    def descrizione(self) -> str:
        return (
            f"Docente: Prof. {self.nome} {self.cognome} (ID: {self.id_dipendente}) | "
            f"Materia: {self.materia_insegnata} | Compenso Mensile: €{self.calcola_compenso_mensile():.2f}"
        )


# ==========================================
# 5. Sottoclasse: Freelance (estende Dipendente)
# ==========================================
class Freelance(Dipendente):
    """
    Sottoclasse di Dipendente specializzata per collaboratori freelance.
    Proprietà specializzanti: partita_iva, tariffa_oraria, ore_lavorate_mese.
    """
    def __init__(
        self,
        nome: str,
        cognome: str,
        eta: int,
        email: str,
        id_dipendente: str,
        data_assunzione: str,
        partita_iva: str,
        tariffa_oraria: float
    ):
        super().__init__(nome, cognome, eta, email, id_dipendente, data_assunzione)
        self.partita_iva = partita_iva
        self.tariffa_oraria = tariffa_oraria
        self.ore_lavorate_mese = 0

    def registra_ore(self, ore: int):
        self.ore_lavorate_mese += ore

    def calcola_compenso_mensile(self) -> float:
        return self.ore_lavorate_mese * self.tariffa_oraria

    def descrizione(self) -> str:
        return (
            f"Freelance: {self.nome} {self.cognome} (P.IVA: {self.partita_iva}) | "
            f"Tariffa: €{self.tariffa_oraria}/h | Ore: {self.ore_lavorate_mese}h | "
            f"Totale Fattura: €{self.calcola_compenso_mensile():.2f}"
        )


# ==========================================
# Test e Dimostrazione
# ==========================================
if __name__ == '__main__':
    print('--- 1. Verifica Classe Astratta (Person) ---')
    try:
        p = Person('Test', 'Person', 25, 'test@test.com')
    except TypeError as e:
        print(f'OK: Person non può essere istanziata direttamente: {e}')

    print('\n--- 2. Verifica Studente ---')
    s = Studente('Luigi', 'Verdi', 21, 'luigi@edu.it', 'MAT12345', 'Informatica')
    s.aggiungi_voto(28)
    s.aggiungi_voto(30)
    print(s.saluta())
    print(s.descrizione())

    print('\n--- 3. Verifica Docente ---')
    d = Docente(
        'Anna', 'Bianchi', 45, 'anna@scuola.it',
        'DOC001', '2018-09-01', 'Matematica', 1800.0
    )
    d.registra_straordinario(10)
    print(d.saluta())
    print(d.descrizione())

    print('\n--- 4. Verifica Freelance ---')
    f = Freelance(
        'Marco', 'Neri', 32, 'marco@freelance.dev',
        'FL099', '2023-01-15', 'IT12345678901', 45.0
    )
    f.registra_ore(40)
    print(f.saluta())
    print(f.descrizione())
