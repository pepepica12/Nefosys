	import { brainCore } from "../brain/index.ts";

export default function brainRoute(app: any) {
  app.post("/brain", async (req: any, res: any) => {
    const input = req.body?.input || "";
    const result = await brainCore(input);
    res.json(result);
  });
}
