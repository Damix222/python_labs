from src.lab08.serialize import students_from_json, students_to_json

inp = "data/lab08/students_input.json"
outp = "data/lab08/students_output.json"

def test_08():
    students = students_from_json(inp)
    print("Студенты загружены:")
    for s in students:
        print(s)

    students_to_json(students, outp)
    print(f"\nСтуденты сохранены в {outp}")

if __name__ == "__main__":
    test_08()
    