import "dotenv/config";
import { db } from "../src/db";
import { todos } from "../src/schema";

export async function seed() {
  await db.insert(todos).values([
    { id: "1", title: "First", done: false },
  ]);
}
