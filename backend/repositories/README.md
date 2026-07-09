# Repositories

Nesta arquitetura de aula, o CRUD simples fica dentro das Models que herdam de `db.Model`.

A pasta `repositories` deve ser usada quando o grupo precisar de consultas que não sejam CRUD básico, por exemplo:

- relatórios;
- filtros complexos;
- consultas com várias tabelas;
- rankings;
- buscas específicas do negócio;
- chamadas de stored procedures do MySQL.

## Exemplo implementado

O arquivo `professor_repository.py` implementa o caso de uso:

```text
buscar_professores_por_disciplina
```

Fluxo esperado:

```text
Controller
↓
Service
↓
Repository
↓
CALL sp_professores_por_disciplina(:disciplina)
↓
MySQL
```

Regra importante: Controller e Service não chamam procedure diretamente. Quem conhece o `CALL sp_...` é o Repository.
