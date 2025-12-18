import { pgTable, text, boolean } from "drizzle-orm/pg-core";

// Definición de la tabla "todos"
export const todos = pgTable("todos", {
  id: text("id").primaryKey(),
  title: text("title").notNull(),
  done: boolean("done").default(false).notNull(),
});
