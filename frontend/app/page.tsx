import { DdosGlobe } from "@/components/DdosGlobe";

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-slate-950 text-slate-100">
      <div className="max-w-5xl w-full px-4 space-y-6">
        <header className="space-y-2 text-center">
          <h1 className="text-3xl md:text-4xl font-semibold">
            Live DDoS Attack Map
          </h1>
          <p className="text-slate-400">
            The first 20 events are simulated for a visual example of how this app works. Events are updated every 30 seconds.
          </p>
        </header>
        <DdosGlobe />
      </div>
    </main>
  );
}
