## Resultado de ejecución (uv run pytest -q)

3 failed, 8 passed, 20 errors in 0.20s

### Fallos previos (no relacionados con el Ejercicio 1)
Los siguientes archivos de pruebas de semanas anteriores presentan errores 
preexistentes, no relacionados con los cambios de este parcial:
- tests/test_week07_models.py
- tests/test_week08_relations.py
- tests/test_week09_queries.py

Causas observadas: fixture 'world' no encontrado en conftest.py, y 
TicketService.__init__() requiere ahora 'repository' y 'users' como 
argumentos obligatorios (constructor cambiado respecto a versiones 
anteriores del proyecto).

### Pruebas del Ejercicio 1 (Etiquetas y encapsulamiento)
tests/test_parcial2_tags.py — PASA correctamente (4/4 pruebas).

(helpdesk-edu) PS C:\Users\Carina Hernandez\Desktop\HelpDesk_EDU> uv run pytest tests/test_parcial2_tags.py -v
======================== test session starts =========================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Carina Hernandez\Desktop\HelpDesk_EDU\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Carina Hernandez\Desktop\HelpDesk_EDU
configfile: pyproject.toml
collected 4 items                                                     

tests/test_parcial2_tags.py::test_add_tag_normalizes_and_avoids_duplicates PASSED [ 25%]
tests/test_parcial2_tags.py::test_add_tag_rejects_blank PASSED  [ 50%]
tests/test_parcial2_tags.py::test_tags_are_independent_between_tickets PASSED [ 75%]
tests/test_parcial2_tags.py::test_tags_assignment_is_rejected PASSED [100%]

========================= 4 passed in 0.03s ==========================
(helpdesk-edu) PS C:\Users\Carina Hernandez\Desktop\HelpDesk_EDU> 


