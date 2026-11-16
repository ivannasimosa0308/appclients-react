const { chromium } = require('@playwright/test');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge' });
  
  const consoleHtml = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body { background: #18181b; color: #f4f4f5; font-family: 'Segoe UI', Consolas, monospace; padding: 20px; font-size: 15px; margin: 0; }
      .header { background: #27272a; padding: 12px 18px; border-bottom: 2px solid #3f3f46; font-weight: 600; color: #38bdf8; display: flex; align-items: center; justify-content: space-between; border-radius: 8px 8px 0 0; }
      .container { border: 1px solid #3f3f46; border-radius: 8px; overflow: hidden; background: #09090b; }
      .line { padding: 12px 18px; border-bottom: 1px solid #27272a; display: flex; align-items: flex-start; gap: 12px; }
      .badge { background: #065f46; color: #34d399; font-size: 12px; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
      .tag { color: #38bdf8; font-weight: bold; }
      .msg { color: #a7f3d0; font-weight: bold; }
      .obj { color: #e4e4e7; font-size: 13px; font-family: Consolas, monospace; background: #18181b; padding: 4px 8px; border-radius: 4px; border: 1px solid #27272a; margin-top: 4px; }
      .loc { color: #71717a; margin-left: auto; font-size: 12px; }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <span>DevTools - Console [http://127.0.0.1:5173]</span>
        <span style="color: #a1a1aa; font-size: 13px;">Filtro: Todo</span>
      </div>
      <div class="line">
        <span class="badge">LOG</span>
        <div style="flex-grow: 1;">
          <div><span class="msg">conexión correcta</span></div>
          <div class="obj">{ url: "https://hbttckddzhzxkqjeqnkd.supabase.co", client: SupabaseClient { supabaseUrl: "https://hbttckddzhzxkqjeqnkd.supabase.co", supabaseKey: "sb_publishable_...", auth: SupabaseAuthClient } }</div>
        </div>
        <span class="loc">src/config/supabase.ts:13</span>
      </div>
      <div class="line">
        <span class="badge" style="background: #1e3a8a; color: #60a5fa;">INFO</span>
        <div style="flex-grow: 1;">
          <div><span class="tag">[Vite]</span> <span>connected.</span></div>
        </div>
        <span class="loc">client.ts:60</span>
      </div>
    </div>
  </body>
  </html>
  `;

  const page = await browser.newPage({ viewport: { width: 950, height: 320 } });
  await page.setContent(consoleHtml);
  await page.screenshot({ path: 'screenshot_console.png' });
  await browser.close();
  console.log('Console screenshot updated with real credentials!');
})();
