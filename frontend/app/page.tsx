import { DdosGlobe } from "@/components/DdosGlobe";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-6xl flex-col gap-8 px-4 py-8 md:flex-row">
        {/* Left side: title + description + stats */}
        <section className="flex w-full flex-col justify-between md:w-2/5">
          <div className="space-y-4">
            <div className="inline-flex items-center gap-2 rounded-full border border-slate-700 bg-slate-900/80 px-3 py-1 text-xs text-slate-400">
              <span className="h-2 w-2 rounded-full bg-emerald-400" />
              Live DDoS Threat Visualizer
            </div>

            <h1 className="text-3xl font-semibold md:text-4xl">
              See suspicious traffic unfold on a{" "}
              <span className="bg-gradient-to-r from-sky-400 to-emerald-400 bg-clip-text text-transparent">
                global 3D map
              </span>
              .
            </h1>

            <p className="text-sm text-slate-400 md:text-base">
              Defensive-only visualization of suspicious IP activity. The
              backend classifies high-confidence DDoS candidates and streams
              them to this interactive globe.
            </p>
          </div>

          <div className="mt-8 grid grid-cols-2 gap-3 text-sm md:grid-cols-3">
            <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-3">
              <div className="text-xs text-slate-400">Backend</div>
              <div className="text-sm font-medium">FastAPI @ :8000</div>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-3">
              <div className="text-xs text-slate-400">Frontend</div>
              <div className="text-sm font-medium">Next.js @ :3000</div>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-3">
              <div className="text-xs text-slate-400">Mode</div>
              <div className="text-sm font-medium">Demo / Fake data</div>
            </div>
          </div>

          <div className="mt-4 text-xs text-slate-500">
            Built with FastAPI, Next.js, Tailwind CSS and the Aceternity GitHub
            Globe component.
          </div>
        </section>

        {/* Right side: globe + panel */}
        <section className="flex w-full flex-1 flex-col gap-4 md:w-3/5">
          <div className="flex-1 rounded-2xl border border-slate-800 bg-slate-900/80 p-3 md:p-4">
            <DdosGlobe />
          </div>

          <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
            <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-3 text-xs">
              <div className="mb-1 font-medium text-slate-200">
                How to read
              </div>
              <p className="text-slate-400">
                Each arc represents suspicious traffic from a source IP (origin)
                to your configured target location.
              </p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-3 text-xs">
              <div className="mb-1 font-medium text-slate-200">
                Arc height &amp; color
              </div>
              <p className="text-slate-400">
                Higher arcs and hotter colors represent a higher internal
                DDoS-confidence score.
              </p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/60 p-3 text-xs">
              <div className="mb-1 font-medium text-slate-200">
                Data source
              </div>
              <p className="text-slate-400">
                Currently using demo events on startup. Replace{" "}
                <code>get_suspicious_ips</code> with your real log pipeline.
              </p>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
