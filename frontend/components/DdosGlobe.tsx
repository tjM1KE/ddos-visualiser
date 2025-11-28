"use client";

import React, { useEffect, useState } from "react";
import dynamic from "next/dynamic";

// Lazy-load the World component on the client only (no SSR)
const World = dynamic(
  () => import("@/components/ui/globe").then((m) => m.World),
  { ssr: false }
);

// Simple types to match what our backend returns
type Position = {
  order: number;
  startLat: number;
  startLng: number;
  endLat: number;
  endLng: number;
  arcAlt: number;
  color: string;
};

type GlobeConfig = {
  pointSize?: number;
  globeColor?: string;
  showAtmosphere?: boolean;
  atmosphereColor?: string;
  atmosphereAltitude?: number;
  emissive?: string;
  emissiveIntensity?: number;
  shininess?: number;
  polygonColor?: string;
  ambientLight?: string;
  directionalLeftLight?: string;
  directionalTopLight?: string;
  pointLight?: string;
  arcTime?: number;
  arcLength?: number;
  rings?: number;
  maxRings?: number;
  initialPosition?: {
    lat: number;
    lng: number;
  };
    autoRotate?: boolean;
    autoRotateSpeed?: number;
};

const globeConfig: GlobeConfig = {
  pointSize: 2,
  globeColor: "#020617",
  showAtmosphere: true,
  atmosphereColor: "#38bdf8",
  atmosphereAltitude: 0.2,
  emissive: "#0ea5e9",
  emissiveIntensity: 0.1,
  shininess: 0.9,
  polygonColor: "#0f172a",
  ambientLight: "#ffffff",
  directionalLeftLight: "#ffffff",
  directionalTopLight: "#ffffff",
  pointLight: "#38bdf8",
  arcTime: 2000,
  arcLength: 0.9,
  rings: 1,
  maxRings: 20,
  initialPosition: { lat: 20, lng: 0 },
  autoRotate: true,
  autoRotateSpeed: 0.9,
};

export function DdosGlobe() {
  const [data, setData] = useState<Position[]>([]);

  useEffect(() => {
    async function fetchArcs() {
      try {
        const res = await fetch("http://127.0.0.1:8000/arcs");
        if (!res.ok) return;
        const json = await res.json();
        setData(json);
      } catch (e) {
        console.error("Failed to fetch arcs", e);
      }
    }

    fetchArcs();
    const id = setInterval(fetchArcs, 30_000);
    return () => clearInterval(id);
  }, []);

  return (
    <div className="w-full h-[600px] rounded-2xl border border-slate-800 bg-slate-950/80">
      {/* Casting to any to avoid fighting types from the generated globe.tsx */}
      <World globeConfig={globeConfig as any} data={data as any} />
    </div>
  );
}
