const API_URL = "http://127.0.0.1:5000/professores";

const formProfessor = document.querySelector("#form-professor");
const professorId = document.querySelector("#professor-id");
const campoNome = document.querySelector("#nome");
const campoEmail = document.querySelector("#email");
const campoDisciplina = document.querySelector("#disciplina");
const tabelaProfessores = document.querySelector("#tabela-professores");
const mensagem = document.querySelector("#mensagem");
const tituloFormulario = document.querySelector("#titulo-formulario");
const botaoSalvar = document.querySelector("#botao-salvar");
const botaoCancelar = document.querySelector("#botao-cancelar");
const botaoRecarregar = document.querySelector("#botao-recarregar");

function mostrarMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = `mensagem ${tipo}`;
}

function limparFormulario() {
    professorId.value = "";
    campoNome.value = "";
    campoEmail.value = "";
    campoDisciplina.value = "";
    tituloFormulario.textContent = "Cadastrar professor";
    botaoSalvar.textContent = "Salvar";
}

async function listarProfessores() {
    try {
        const resposta = await fetch(API_URL);
        const professores = await resposta.json();

        tabelaProfessores.innerHTML = "";

        if (professores.length === 0) {
            tabelaProfessores.innerHTML = `
                <tr>
                    <td colspan="5">Nenhum professor cadastrado.</td>
                </tr>
            `;
            return;
        }

        professores.forEach((professor) => {
            const linha = document.createElement("tr");

            linha.innerHTML = `
                <td data-label="ID">${professor.id}</td>
                <td data-label="Nome">${professor.nome}</td>
                <td data-label="E-mail">${professor.email}</td>
                <td data-label="Disciplina">${professor.disciplina}</td>
                <td data-label="Ações">
                    <div class="acoes-tabela">
                        <button onclick='prepararEdicao(${JSON.stringify(professor)})'>Editar</button>
                        <button class="perigo" onclick="deletarProfessor(${professor.id})">Excluir</button>
                    </div>
                </td>
            `;

            tabelaProfessores.appendChild(linha);
        });
    } catch (erro) {
        mostrarMensagem("Não foi possível carregar os professores. Verifique se a API está rodando.", "erro");
    }
}

function prepararEdicao(professor) {
    professorId.value = professor.id;
    campoNome.value = professor.nome;
    campoEmail.value = professor.email;
    campoDisciplina.value = professor.disciplina;
    tituloFormulario.textContent = "Editar professor";
    botaoSalvar.textContent = "Atualizar";
    mostrarMensagem("Editando professor selecionado.", "sucesso");
}

async function salvarProfessor(evento) {
    evento.preventDefault();

    const dados = {
        nome: campoNome.value,
        email: campoEmail.value,
        disciplina: campoDisciplina.value,
    };

    const id = professorId.value;
    const metodo = id ? "PUT" : "POST";
    const url = id ? `${API_URL}/${id}` : API_URL;

    try {
        const resposta = await fetch(url, {
            method: metodo,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dados),
        });

        if (!resposta.ok) {
            const erro = await resposta.json();
            mostrarMensagem(erro.erro || "Erro ao salvar professor.", "erro");
            return;
        }

        mostrarMensagem(id ? "Professor atualizado com sucesso." : "Professor cadastrado com sucesso.", "sucesso");
        limparFormulario();
        listarProfessores();
    } catch (erro) {
        mostrarMensagem("Erro de conexão com a API.", "erro");
    }
}

async function deletarProfessor(id) {
    const confirmar = confirm("Deseja realmente excluir este professor?");

    if (!confirmar) {
        return;
    }

    try {
        const resposta = await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });

        if (!resposta.ok) {
            const erro = await resposta.json();
            mostrarMensagem(erro.erro || "Erro ao excluir professor.", "erro");
            return;
        }

        mostrarMensagem("Professor excluído com sucesso.", "sucesso");
        listarProfessores();
    } catch (erro) {
        mostrarMensagem("Erro de conexão com a API.", "erro");
    }
}

formProfessor.addEventListener("submit", salvarProfessor);
botaoCancelar.addEventListener("click", limparFormulario);
botaoRecarregar.addEventListener("click", listarProfessores);

listarProfessores();
