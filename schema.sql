-- Crear esquemas
CREATE SCHEMA "public";
CREATE SCHEMA "auth";
CREATE SCHEMA "neon_auth";
CREATE SCHEMA "pgrst";

-- Tabla de pruebas
CREATE TABLE "playing_with_neon" (
    "id" serial PRIMARY KEY,
    "name" text NOT NULL,
    "value" real
);

-- Tabla de sincronización de usuarios
CREATE TABLE "neon_auth"."users_sync" (
    "raw_json" jsonb NOT NULL,

    -- Columnas generadas a partir de raw_json
    "id" text PRIMARY KEY
        GENERATED ALWAYS AS ((raw_json ->> 'id')) STORED,

    "name" text
        GENERATED ALWAYS AS ((raw_json ->> 'display_name')) STORED,

    "email" text
        GENERATED ALWAYS AS ((raw_json ->> 'primary_email')) STORED,

    "created_at" timestamptz
        GENERATED ALWAYS AS (
            to_timestamp(
                trunc(((raw_json ->> 'signed_up_at_millis')::bigint / 1000))
            )
        ) STORED,

    "updated_at" timestamptz,
    "deleted_at" timestamptz
);

-- Índices
CREATE UNIQUE INDEX "playing_with_neon_pkey"
    ON "playing_with_neon" ("id");

CREATE INDEX "users_sync_deleted_at_idx"
    ON "neon_auth"."users_sync" ("deleted_at");

CREATE UNIQUE INDEX "users_sync_pkey"
    ON "neon_auth"."users_sync" ("id");
