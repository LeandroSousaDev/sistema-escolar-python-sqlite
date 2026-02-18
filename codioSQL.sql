-- Tabela: Aluno
DROP TABLE IF EXISTS Aluno;
CREATE TABLE IF NOT EXISTS `Aluno` (
  `id_aluno` INTEGER PRIMARY KEY AUTOINCREMENT,
  `nome` VARCHAR(100) NULL,
  `cpf` VARCHAR(11) NULL,
  `data_nascimento` VARCHAR(10) NULL,
  `Curso_id_curso` INT NOT NULL,
  CONSTRAINT `fk_Aluno_Curso1`
    FOREIGN KEY (`Curso_id_curso`)
    REFERENCES `Curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

DROP TABLE IF EXISTS Professor;
CREATE TABLE IF NOT EXISTS `Professor` (
  `id_professor` INTEGER AUTO INCREMENT not null,
  `nome` VARCHAR(100) NULL,
  `formacao` VARCHAR(45) NULL,
  PRIMARY KEY (`id_professor`))

-- Tabela: Contrato
DROP TABLE IF EXISTS Contrato;
CREATE TABLE IF NOT EXISTS `Contrato` (
  `id_contrato` INTEGER PRIMARY KEY AUTOINCREMENT,
  `vinculo` VARCHAR(45) NULL,
  `carga_horaria_semanal` VARCHAR(45) NULL,
  `Professor_id_professor` INT NOT NULL,

  CONSTRAINT `fk_Contrato_Professor1`
    FOREIGN KEY (`Professor_id_professor`)
    REFERENCES `Professor` (`id_professor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- Tabela: Curso
DROP TABLE IF EXISTS Curso;
CREATE TABLE IF NOT EXISTS `Curso` (
  `id_curso` INTEGER PRIMARY KEY AUTOINCREMENT,
  `nome` VARCHAR(45) NULL,
  `carga_horaria` INT NULL);

-- Tabela: Professor_Curso
DROP TABLE IF EXISTS Professor_Curso;
CREATE TABLE IF NOT EXISTS `Professor_Curso` (
  `Professor_id_professor` INT NOT NULL,
  `Curso_id_curso` INT NOT NULL,
  PRIMARY KEY (`Professor_id_professor`, `Curso_id_curso`),

  CONSTRAINT `fk_Professor_has_Curso_Professor1`
    FOREIGN KEY (`Professor_id_professor`)
    REFERENCES `Professor` (`id_professor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Professor_has_Curso_Curso1`
    FOREIGN KEY (`Curso_id_curso`)
    REFERENCES `Curso` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- Tabela: Prontuario
DROP TABLE IF EXISTS Prontuario;
CREATE TABLE IF NOT EXISTS `Prontuario` (
  `id_prontuario` INTEGER PRIMARY KEY AUTOINCREMENT,
  `data_matricula` VARCHAR(10) NULL,
  `situacao_matricula` VARCHAR(45) NULL,
  `Aluno_id_aluno` INT NOT NULL,


  CONSTRAINT `fk_Prontuario_Aluno`
    FOREIGN KEY (`Aluno_id_aluno`)
    REFERENCES `Aluno` (`id_aluno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

