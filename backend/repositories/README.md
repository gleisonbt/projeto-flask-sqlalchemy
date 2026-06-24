# Repositories

Nesta arquitetura de aula, o CRUD simples fica dentro das Models que herdam de `db.Model`.

A pasta `repositories` foi mantida porque faz parte da estrutura esperada do projeto. Ela deve ser usada quando o grupo precisar de consultas que não sejam CRUD básico, por exemplo:

- relatórios;
- filtros complexos;
- consultas com várias tabelas;
- rankings;
- buscas específicas do negócio.
