import { callRailway } from "./connectors/railway.ts";
import { checkTelemetry } from "./connectors/telemetry.ts";

export async function brainCore(input: string) {
  const telemetry = await checkTelemetry();

  const railwayResponse = await callRailway("/brain", { input });

  return {
    status: "ok",
    input,
    telemetry,
    railway: railwayResponse
  };
}
