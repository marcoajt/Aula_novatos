# https://exercism.org/tracks/python/exercises/grade-school


class School:
    """Representa o cadastro de alunos por série (grade) de uma escola."""

    def __init__(self) -> None:
        """Inicializa a escola com estrutura vazia para séries e histórico de adições."""
        # grade -> conjunto de alunos
        self._grades: dict[int, set[str]] = (
            {}
        )  # set ajuda a evitar (sobrescrever) duplicados os nomes do aluno, porém as serie pode repetir.
        # histórico dos resultados de cada chamada de add_student
        self._added_results: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """Adiciona um aluno a uma série, se ainda não existir em nenhuma série.

        :param name: str - nome do aluno.
        :param grade: int - série (ano) em que o aluno será matriculado.
        """
        # se o aluno já estiver em qualquer série, não adiciona de novo
        for students in self._grades.values():
            if name in students:
                self._added_results.append(False)
                return

        # garante que a série exista, cria a serie se não existir
        if grade not in self._grades:
            self._grades[grade] = set()

        # adiciona o aluno na série
        self._grades[grade].add(name)
        self._added_results.append(True)

    def roster(self) -> list[str]:
        """Retorna a lista completa de alunos, ordenada por série e por nome.

        :return: list[str] - alunos em ordem de série crescente e, dentro da série, ordem alfabética.
        """
        result: list[str] = []
        for grade in sorted(self._grades.keys()):
            result.extend(sorted(self._grades[grade]))
        return result

    def grade(self, grade_number: int) -> list[str]:
        """Retorna a lista de alunos de uma série específica, em ordem alfabética.

        :param grade_number: int - série consultada.
        :return: list[str] - alunos dessa série ou lista vazia se não houver alunos.
        """
        if grade_number not in self._grades:
            return []
        return sorted(self._grades[grade_number])

    def added(self) -> list[bool]:
        """Retorna o histórico de sucesso das chamadas de add_student.

        :return: list[bool] - True se o aluno foi adicionado, False se foi rejeitado.
        """
        return self._added_results
