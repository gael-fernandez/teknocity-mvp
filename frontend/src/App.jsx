import { useState, useEffect } from "react"
import { MapContainer, TileLayer, CircleMarker, Popup } from "react-leaflet"
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts"

export default function App() {
const [simulacionActiva, setSimulacionActiva] = useState(true)
const [semaforos, setSemaforos] = useState([
  // Av. Vallarta frente al estadio
  { id: 1, position: [20.695689, -103.454978], fase: "verde", congestion: 40 },

  // Periférico Poniente
  { id: 2, position: [20.671,-103.435], fase: "rojo", congestion: 65 },

  // Av. Aviación
  { id: 3, position: [20.702203, -103.460341], fase: "amarillo", congestion: 55 },

  // Av. Santa Margarita
  { id: 4, position: [20.731126, -103.451358], fase: "verde", congestion: 30 }
])

  const [historial, setHistorial] = useState([])

  useEffect(() => {
  if (!simulacionActiva) return

  const interval = setInterval(() => {

    setSemaforos(prev => {
 const nuevosSemaforos = prev.map(s => {

  const nuevaCongestion = Math.floor(Math.random() * 101)

  let nuevaFase

  if (nuevaCongestion > 70) {
    nuevaFase = "verde"
  } else if (nuevaCongestion < 30) {
    nuevaFase = "rojo"
  } else {
    nuevaFase = "amarillo"
  }

  return {
    ...s,
    congestion: nuevaCongestion,
    fase: nuevaFase
  }
})

      const promedio =
        nuevosSemaforos.reduce((acc, s) => acc + s.congestion, 0) /
        nuevosSemaforos.length

      setHistorial(h => {
        const nuevoDato = {
          tiempo: new Date().toLocaleTimeString(),
          congestion: Math.floor(promedio)
        }

        const nuevoHistorial = [...h, nuevoDato]
        if (nuevoHistorial.length > 10) nuevoHistorial.shift()

        return nuevoHistorial
      })

      return nuevosSemaforos
    })

  }, 4000)

  return () => clearInterval(interval)

}, [simulacionActiva])
const congestionPromedio = (
  semaforos.reduce((acc, s) => acc + s.congestion, 0) / semaforos.length
).toFixed(1)

const enRojo = semaforos.filter(s => s.fase === "rojo").length

const congestionAlta = semaforos.find(s => s.congestion > 80)

const hayAlerta = Boolean(congestionAlta)
  let mensajeIA = "Sistema funcionando con normalidad 🚦"

  if (congestionAlta) {
    mensajeIA = `
Alta congestión detectada en semáforo ${congestionAlta.id}.
Recomendación: extender fase verde.
Reducción estimada de espera: 12%.
`
  }

  const colorFase = (fase) => {
    if (fase === "verde") return "green"
    if (fase === "amarillo") return "yellow"
    return "red"
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white p-4">
      <div className="grid grid-cols-3 grid-rows-[1fr_1fr_1fr_auto]">

        {/* MAPA */}
        <div className="col-span-2 row-span-3 bg-gray-800 rounded-2xl overflow-hidden max-h-[600px]">
          <h2 className="text-xl font-bold mb-2">Mapa en tiempo real</h2>

          <MapContainer
            center={[20.6810, -103.4600]}
            zoom={13}
            scrollWheelZoom={true}
            className="h-full w-full rounded-xl"
          >
            <TileLayer
              attribution='&copy; OpenStreetMap contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {semaforos.map(semaforo => (
              <CircleMarker
                key={semaforo.id}
                center={semaforo.position}
                radius={8 + semaforo.congestion / 10}
                pathOptions={{ color: colorFase(semaforo.fase) }}
              >
                <Popup>
                  Semáforo {semaforo.id} <br />
                  Fase: {semaforo.fase} <br />
                  Congestión: {semaforo.congestion}%
                </Popup>
              </CircleMarker>
            ))}
          </MapContainer>
        </div>

        {/* MÉTRICAS */}
<div className="flex gap-2 flex-wrap">
  <button
    onClick={() => setSimulacionActiva(false)}
    className="bg-yellow-600 hover:bg-yellow-500 px-3 py-2 rounded-lg"
  >
    ⏸ Pausar
  </button>

  <button
    onClick={() => setSimulacionActiva(true)}
    className="bg-green-600 hover:bg-green-500 px-3 py-2 rounded-lg"
  >
    ▶ Reanudar
  </button>

  <button
    onClick={() => setHistorial([])}
    className="bg-blue-600 hover:bg-blue-500 px-3 py-2 rounded-lg"
  >
    🔄 Reset Historial
  </button>
</div>
        <div className="col-span-1 row-span-3 bg-gray-800 rounded-2xl p-4 flex flex-col gap-4">
          <h2 className="text-xl font-bold">Métricas</h2>

          <div className="bg-gray-700 p-4 rounded-xl">
            Semáforos activos: {semaforos.length}
          </div>

          <div className="bg-gray-700 p-4 rounded-xl">
            Congestión promedio: {congestionPromedio}%
          </div>

          <div className="bg-gray-700 p-4 rounded-xl">
            Semáforos en rojo: {enRojo}
          </div>

          <div className="bg-gray-700 p-4 rounded-xl h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={historial}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="tiempo" hide />
                <YAxis domain={[0, 100]} />
                <Tooltip />
                <Line type="monotone" dataKey="congestion" stroke="#22c55e" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* PANEL IA */}
        <div
          className={`col-span-3 row-span-1 rounded-2xl p-4 transition-all duration-500 ${
            hayAlerta ? "bg-red-900 animate-pulse" : "bg-gray-800"
          }`}
        >
          <p className="mt-2 text-sm">
            {hayAlerta
              ? `⚠️ Congestión crítica en semáforo ${congestionAlta?.id} (${congestionAlta?.congestion}%).`
              : "✔️ Flujo vehicular estable. Sin anomalías detectadas."}
          </p>

          <div
            className={`p-4 rounded-xl whitespace-pre-line ${
              hayAlerta ? "bg-red-700" : "bg-gray-700"
            }`}
          >
            {mensajeIA}
          </div>
        </div>

      </div>
    </div>
  )
}