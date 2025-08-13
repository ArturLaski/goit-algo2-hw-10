from dataclasses import dataclass, field
from typing import Set, List, Optional

@dataclass
class Teacher:
    """
    Klasa reprezentująca nauczyciela.
    """
    first_name: str
    last_name: str
    age: int
    email: str
    can_teach_subjects: Set[str]
    assigned_subjects: Set[str] = field(default_factory=set)


def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> Optional[List[Teacher]]:
    """
    Tworzy plan zajęć, przydzielając nauczycieli w taki sposób,
    aby zminimalizować ich liczbę i pokryć wszystkie przedmioty.
    """
    schedule = []  # Ostateczna lista nauczycieli z przydzielonymi przedmiotami
    uncovered_subjects = subjects.copy()  # Zbiór niepokrytych przedmiotów

    while uncovered_subjects:
        # Znaleźć nauczyciela, który pokrywa najwięcej niepokrytych przedmiotów,
        # a w przypadku remisu — najmłodszego
        best_teacher: Optional[Teacher] = None
        best_cover: Set[str] = set()

        for teacher in teachers:
            cover = teacher.can_teach_subjects & uncovered_subjects
            if len(cover) > len(best_cover) or (
                    len(cover) == len(best_cover) and teacher.age < (best_teacher.age if best_teacher else float('inf'))):
                best_teacher = teacher
                best_cover = cover

        if not best_cover:  # Jeśli nie można już pokryć przedmiotów
            return None

        # Przydzielić przedmioty nauczycielowi
        best_teacher.assigned_subjects = best_cover
        schedule.append(best_teacher)
        uncovered_subjects -= best_cover

    return schedule


if __name__ == '__main__':
    subjects = {'Matematyka', 'Fizyka', 'Chemia', 'Informatyka', 'Biologia'}
    teachers = [
        Teacher("Aleksander", "Iwanenko", 45, "o.ivanenko@example.com", {"Matematyka", "Fizyka"}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemia"}),
        Teacher("Sergiusz", "Kowalenko", 50, "s.kowalenko@example.com", {"Informatyka", "Matematyka"}),
        Teacher("Natalia", "Szewczenko", 29, "n.szewczenko@example.com", {"Biologia", "Chemia"}),
        Teacher("Dymitr", "Bondarenko", 35, "d.bondarenko@example.com", {"Fizyka", "Informatyka"}),
        Teacher("Olena", "Hrycenko", 4
