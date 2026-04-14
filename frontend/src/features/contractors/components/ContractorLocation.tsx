import "leaflet/dist/leaflet.css";
import L from "leaflet";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";
import { MapContainer, Marker, TileLayer, Popup } from "react-leaflet";

delete (L.Icon.Default.prototype as L.Icon.Default & {
    _getIconUrl?: () => string;
})._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: markerIcon2x,
    iconUrl: markerIcon,
    shadowUrl: markerShadow,
});

type ContractorLocationProps = {
    contractorName?: string;
    lastUpdated?: string;
};

export default function ContractorLocation({
    contractorName,
    lastUpdated,
}: ContractorLocationProps) {
    const position: [number, number] = [31.9686, -99.9018];

    return (
        <section className="rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-[#2F4F75]">Current Location</h3>
                <p className="text-sm text-[#4A6C8A]">Live contractor location and dispatch visibility.</p>
            </div>

            <div className="h-168 overflow-hidden rounded-xl border border-[#2F4F75]">
                <MapContainer
                    center={position}
                    zoom={6}
                    scrollWheelZoom={false}
                    className="h-full w-full"
                    >
                    <TileLayer
                        attribution="&copy; OpenStreetMap contributors"
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <Marker position={position}>
                        <Popup>{contractorName} is currently at pinned location.</Popup>
                    </Marker>
                </MapContainer>
            </div>

            <p className="mt-4 text-sm text-[#4A6C8A]">{lastUpdated}</p>
        </section>
    );
}