PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  rol TEXT NOT NULL
);
INSERT INTO usuarios VALUES(1,'Osvaldo','admin');
INSERT INTO usuarios VALUES(2,'Osvaldo','admin');
CREATE TABLE proyectos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  descripcion TEXT,
  responsable_id INTEGER,
  FOREIGN KEY(responsable_id) REFERENCES usuarios(id)
);
INSERT INTO proyectos VALUES(1,'Proyecto Neón','Integración con PinFlo',1);
CREATE TABLE auditoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usuario TEXT,
  accion TEXT,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO auditoria VALUES(1,'Osvaldo','Creación inicial','2025-12-10 22:46:49');
PRAGMA writable_schema=ON;
CREATE TABLE IF NOT EXISTS sqlite_sequence(name,seq);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('usuarios',2);
INSERT INTO sqlite_sequence VALUES('proyectos',1);
INSERT INTO sqlite_sequence VALUES('auditoria',1);
PRAGMA writable_schema=OFF;
COMMIT;
