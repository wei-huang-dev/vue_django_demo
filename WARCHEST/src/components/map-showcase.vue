<!-- <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
     integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
     crossorigin=""/> -->

<template>
<div>
    <div>
        <v-btn name="button" @click="fitPolyline" color="rgb(202, 216, 243)">
            Fit map to polyline
        </v-btn><br><br>
        Zoom: level
        <input class="style-1" v-model.number="zoom" type="number">
        position:
        <select v-model="zoomPosition" class="style-1">
            <option v-for="(position, index) in Positions" :key="index" :value="position">
                {{ position }}
            </option>
        </select>
        <br>
        Center : <span> {{ center }} </span><br>
        Bounds : <span> {{ bounds }} </span><br>
        Contol Layers position:
        <select v-model="layersPosition" class="style-1">
            <option v-for="(position, index) in Positions" :key="index" :value="position">
                {{ position }}
            </option>
        </select>
        Attribution position:
        <select v-model="attributionPosition" class="style-1">
            <option v-for="(position, index) in Positions" :key="index" :value="position">
                {{ position }}
            </option>
        </select>
        <hr>
        <v-btn name="button" @click="addEllipse" color="rgb(202, 216, 243)">
            Add ellipses
        </v-btn><br>
        <hr>
        <v-btn name="button" @click="addMarker" color="rgb(202, 216, 243)">
            Add a marker
        </v-btn><br>
        <table>
            <tr>
                <th>Marker</th>
                <th>Latitude</th>
                <th>Longitude</th>
                <th>Tooltip</th>
                <th>Is Draggable ?</th>
                <th>Is Visible ?</th>
                <th>Remove</th>
            </tr>
            <tr v-for="(item, index) in markers" :key="index">
                <td>{{ 'Marker ' + (index + 1) }}</td>
                <td>
                    <input v-model.number="item.position.lat" type="number">
                </td>
                <td>
                    <input v-model.number="item.position.lng" type="number">
                </td>
                <td>
                    <input v-model="item.tooltip" type="text">
                </td>
                <td style="text-align: center">
                    <input v-model="item.draggable" type="checkbox">
                </td>
                <td style="text-align: center">
                    <input v-model="item.visible" type="checkbox">
                </td>
                <td style="text-align: center">
                    <input type="button" value="X" @click="removeMarker(index)">
                </td>
            </tr>
        </table>
        <hr>
        <table>
            <tr>
                <th>Layer</th>
                <th>-Is Visible?</th>
                <th>-Are Markers visible?</th>
                <th>-Is Polyline visible?</th>
            </tr>
            <tr v-for="(item, index) in stuff" :key="index">
                <td>{{ 'Layer ' + (index + 1) }}</td>
                <td style="text-align: center">
                    <input v-model="item.visible" type="checkbox">
                </td>
                <td style="text-align: center">
                    <input v-model="item.markersVisible" type="checkbox">
                </td>
                <td style="text-align: center">
                    <input v-model="item.polyline.visible" type="checkbox">
                </td>
            </tr>
        </table>
    </div>
    <l-map ref="map" @ready="onReady()" :zoom.sync="zoom" :options="mapOptions" :center="center" :bounds="bounds" :min-zoom="minZoom" :max-zoom="maxZoom" style="height: 500px; width: 100%">
        <l-control-layers :position="layersPosition" :collapsed="false" :sort-layers="true" />
        <l-tile-layer v-for="tileProvider in tileProviders" :key="tileProvider.name" :name="tileProvider.name" :visible="tileProvider.visible" :url="tileProvider.url" :attribution="tileProvider.attribution" :token="token" layer-type="base" />
        <l-control-zoom :position="zoomPosition" />
        <l-control-attribution :position="attributionPosition" :prefix="attributionPrefix" />
        <l-control-scale :imperial="imperial" />
        <l-marker v-for="marker in markers" :key="marker.id" :visible="marker.visible" :draggable="marker.draggable" :lat-lng.sync="marker.position" :icon="marker.icon" @click="alert(marker)">
            <l-popup :content="marker.tooltip" />
            <l-tooltip :content="marker.tooltip" />
        </l-marker>
        <l-layer-group layer-type="overlay" name="Layer polyline">
            <l-polyline v-for="item in polylines" :key="item.id" :lat-lngs="item.points" :visible="item.visible" @click="alert(item)" />
        </l-layer-group>
        <l-layer-group v-for="item in stuff" :key="item.id" :visible.sync="item.visible" layer-type="overlay" name="Layer 1">
            <l-layer-group :visible="item.markersVisible">
                <l-marker v-for="marker in item.markers" :key="marker.id" :visible="marker.visible" :draggable="marker.draggable" :lat-lng="marker.position" @click="alert(marker)" />
            </l-layer-group>
            <l-polyline :lat-lngs="item.polyline.points" :visible="item.polyline.visible" @click="alert(item.polyline)" />
        </l-layer-group>
        <l-circle :lat-lng="circle.center" :radius="circle.radius" :color="red">
            <l-popup :content="Circle" />
        </l-circle>
    </l-map>

</div>
</template>

<script>
import * as theEllipse from "../helpers/l.ellipse.js"; // !magic
import {
    latLng,
    latLngBounds
} from "leaflet";
import {
    LMap,
    LTileLayer,
    LMarker,
    LCircle,
    LPolyline,
    LLayerGroup,
    LTooltip,
    LPopup,
    LControlZoom,
    LControlAttribution,
    LControlScale,
    LControlLayers
} from 'vue2-leaflet';

const markers1 = [{
        position: {
            lng: -1.219482,
            lat: 47.41322
        },
        visible: true,
        draggable: true,
    },
    {
        position: {
            lng: -1.571045,
            lat: 47.457809
        }
    },
    {
        position: {
            lng: -1.560059,
            lat: 47.739323
        }
    },
    {
        position: {
            lng: -0.922852,
            lat: 47.886881
        }
    },
    {
        position: {
            lng: -0.769043,
            lat: 48.231991
        }
    },
    {
        position: {
            lng: 0.395508,
            lat: 48.268569
        }
    },
    {
        position: {
            lng: 0.604248,
            lat: 48.026672
        }
    },
    {
        position: {
            lng: 1.2854,
            lat: 47.982568
        }
    },
    {
        position: {
            lng: 1.318359,
            lat: 47.894248
        }
    },
    {
        position: {
            lng: 1.373291,
            lat: 47.879513
        }
    },
    {
        position: {
            lng: 1.384277,
            lat: 47.798397
        }
    },
    {
        position: {
            lng: 1.329346,
            lat: 47.754098
        }
    },
    {
        position: {
            lng: 1.329346,
            lat: 47.680183
        }
    },
    {
        position: {
            lng: 0.999756,
            lat: 47.635784
        }
    },
    {
        position: {
            lng: 0.86792,
            lat: 47.820532
        }
    },
    {
        position: {
            lng: 0.571289,
            lat: 47.820532
        }
    },
    {
        position: {
            lng: 0.439453,
            lat: 47.717154
        }
    },
    {
        position: {
            lng: 0.439453,
            lat: 47.61357
        }
    },
    {
        position: {
            lng: -0.571289,
            lat: 47.487513
        }
    },
    {
        position: {
            lng: -0.615234,
            lat: 47.680183
        }
    },
    {
        position: {
            lng: -0.812988,
            lat: 47.724545
        }
    },
    {
        position: {
            lng: -1.054688,
            lat: 47.680183
        }
    },
    {
        position: {
            lng: -1.219482,
            lat: 47.41322
        }
    },
];

const poly1 = [{
        lng: -1.219482,
        lat: 47.41322
    },
    {
        lng: -1.571045,
        lat: 47.457809
    },
    {
        lng: -1.560059,
        lat: 47.739323
    },
    {
        lng: -0.922852,
        lat: 47.886881
    },
    {
        lng: -0.769043,
        lat: 48.231991
    },
    {
        lng: 0.395508,
        lat: 48.268569
    },
    {
        lng: 0.604248,
        lat: 48.026672
    },
    {
        lng: 1.2854,
        lat: 47.982568
    },
    {
        lng: 1.318359,
        lat: 47.894248
    },
    {
        lng: 1.373291,
        lat: 47.879513
    },
    {
        lng: 1.384277,
        lat: 47.798397
    },
    {
        lng: 1.329346,
        lat: 47.754098
    },
    {
        lng: 1.329346,
        lat: 47.680183
    },
    {
        lng: 0.999756,
        lat: 47.635784
    },
    {
        lng: 0.86792,
        lat: 47.820532
    },
    {
        lng: 0.571289,
        lat: 47.820532
    },
    {
        lng: 0.439453,
        lat: 47.717154
    },
    {
        lng: 0.439453,
        lat: 47.61357
    },
    {
        lng: -0.571289,
        lat: 47.487513
    },
    {
        lng: -0.615234,
        lat: 47.680183
    },
    {
        lng: -0.812988,
        lat: 47.724545
    },
    {
        lng: -1.054688,
        lat: 47.680183
    },
    {
        lng: -1.219482,
        lat: 47.41322
    },
];

const tileProviders = [{
        name: 'OpenStreetMap',
        visible: true,
        attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', // online
    },
    {
        name: 'Offline Map',
        visible: true,
        attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        // url: '/LeMans/OSMPublicTransport/{z}/{x}/{y}.png', // offline
        url: '/LondonLeMans/OSMPublicTransport/{z}/{x}/{y}.png', // offline
    },
    {
        name: 'OpenTopoMap',
        visible: false,
        url: 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
    },
];

export default {
    name: 'Example',
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LCircle,
        LPolyline,
        LLayerGroup,
        LTooltip,
        LPopup,
        LControlZoom,
        LControlAttribution,
        LControlScale,
        LControlLayers,
    },
    data() {
        return {
            map: null,
            center: [47.695, -0.615],
            opacity: 0.6,
            token: 'your token if using mapbox',
            mapOptions: {
                zoomControl: false,
                attributionControl: false,
                zoomSnap: true,
            },
            zoom: 10,
            minZoom: 1,
            maxZoom: 20, // force to default
            zoomPosition: 'topleft',
            attributionPosition: 'bottomright',
            layersPosition: 'topright',
            attributionPrefix: 'Vue2Leaflet',
            imperial: false,
            Positions: ['topleft', 'topright', 'bottomleft', 'bottomright'],
            tileProviders: tileProviders,
            circle: {
                center: latLng(47.886881, -0.922852),
                radius: 4500
            },
            ellipse: null,
            markers: [{
                    id: 'm1',
                    // position: { lat: 51.505, lng: -0.09 },
                    position: {
                        lat: 22.275,
                        lng: 114.16
                    },
                    tooltip: 'tooltip for marker1',
                    draggable: true,
                    visible: true,
                },
                {
                    id: 'm2',
                    //          position: { lat: 51.8905, lng: -0.09 },
                    position: {
                        lat: 60.05,
                        lng: -2.09
                    },
                    tooltip: 'tooltip for marker2',
                    draggable: true,
                    visible: false,
                },
                {
                    id: 'm3',
                    position: {
                        lat: 51.005,
                        lng: -0.09
                    },
                    tooltip: 'tooltip for marker3',
                    draggable: true,
                    visible: true,
                },
                {
                    id: 'm4',
                    position: {
                        lat: 50.7605,
                        lng: -0.09
                    },
                    tooltip: 'tooltip for marker4',
                    draggable: true,
                    visible: false,
                },
            ],
            polylines: [{
                    id: 'p1',
                    points: [{
                            lat: 37.772,
                            lng: -122.214
                        },
                        {
                            lat: 21.291,
                            lng: -157.821
                        },
                        {
                            lat: -18.142,
                            lng: -181.569
                        },
                        {
                            lat: -27.467,
                            lng: -206.973
                        },
                    ],
                    visible: true,
                },
                {
                    id: 'p2',
                    points: [
                        [-73.91, 40.78],
                        [-87.62, 41.83],
                        [-96.72, 32.76],
                    ],
                    visible: true,
                },
            ],
            stuff: [{
                id: 's1',
                markers: markers1,
                polyline: {
                    points: poly1,
                    visible: true
                },
                visible: true,
                markersVisible: true,
                offline: false,
            }, ],
            bounds: latLngBounds({
                lat: 51.476483373501964,
                lng: -0.14668464136775586
            }, {
                lat: 51.52948330894063,
                lng: -0.019140238291583955
            }),
        };
    },
    methods: {
        mounted() {
            this.$nextTick(() => {
                this.map = this.$refs.map.mapObject
            })
        },
        onReady() {
            this.map = this.$refs.map.mapObject
            this.map.on('click', this.onMapClick);
        },
        alert(item) {
            alert('this is ' + JSON.stringify(item));
        },
        addEllipse: function () {

            L.ellipse([47.86, -0.92], [900, 500], 70, {
                color: 'red',
                fillOpacity: 0.2
            }).addTo(this.map);
            L.ellipse([47.68, -0.612], [1300, 340], 112, {
                color: 'brown',
                fillOpacity: 0.2
            }).addTo(this.map);
            L.ellipse([47.72, -0.833], [939, 531], 107, {
                color: 'purple',
                fillOpacity: 0.2
            }).addTo(this.map);
            L.ellipse([47.656, -0.90], [977, 432], 109).addTo(this.map);
            L.ellipse([60, -3.2], [1300, 340], 112).addTo(this.map);
            L.ellipse([55, -3.3], [939, 531], 107).addTo(this.map);
            L.ellipse([56, -3.4], [977, 432], 109).addTo(this.map);
        },
        addMarker: function () {
            const newMarker = {
                position: {
                    lat: 50.5505,
                    lng: -0.09
                },
                draggable: true,
                visible: true,
            };
            this.markers.push(newMarker);
        },
        removeMarker: function (index) {
            this.markers.splice(index, 1);
        },
        fitPolyline: function () {
            const bounds = latLngBounds(markers1.map(o => o.position));
            this.bounds = bounds;
        },
        onMapClick: function (e) {
            console.log(e.latlng.toString())
        }
    },
};
</script>
