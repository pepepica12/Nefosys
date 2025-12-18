import "dotenv/config";
import { migrate } from "drizzle-orm/neon-http/migrator";
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "../src/schema";

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql, { schema });

async function main() {
  await migrate(db as any, { migrationsFolder: "drizzle" });
}

main().then(() => process.exit(0)).catch(err => {
  console.error(err);
  process.exit(1);
});
