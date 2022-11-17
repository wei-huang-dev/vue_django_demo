<template>
<l-map :center="center" :zoom="zoom" class="map" ref="map" @update:zoom="zoomUpdated" @update:center="centerUpdated">
    <l-tile-layer :url="url">
    </l-tile-layer>
    <restaurant v-for="marker in markers" :key="marker.id" :marker="marker">
    </restaurant>
    <!-- <restaurant-circle v-for="r_circle in r_circles" :key="r_circle.id" :r_circle="r_circle">
    </restaurant-circle> -->
</l-map>
</template>

<script>
import {
    LMap,
    LTileLayer
} from 'vue2-leaflet';
import Restaurant from './restaurant'
import 'leaflet/dist/leaflet.css';

export default {
    components: {
        LMap,
        LTileLayer,
        Restaurant
    },
    data() {
        return {
// https://xerocrypt.github.io/articles/offline-maps.html
// https://github.com/davidrs/phonegap-3.0-leaflet/blob/master/www/js/index.js
// file:///C:/Users/d-nick.hoang/phonegap-3.0-leaflet/www/index.html
// https://wiki.osgeo.org/wiki/Tile_Map_Service_Specification
// https://mobac.sourceforge.io/
// https://tomik23.github.io/leaflet-examples/
// https://vue2-leaflet.netlify.app/examples/

            url: '/img/mapTiles/{z}/{x}/{y}.png',
            center: [45.423, -75.769],
            zoom: 12,
            markers: [{
                    id: 1,
                    imageUrl: 'https://img.icons8.com/doodle/48/000000/fish-food--v1.png',
                    coordinates: [45.443, -75.669]
                },
                {
                    id: 2,
                    imageUrl: 'https://img.icons8.com/doodle/48/000000/pizza--v1.png',
                    coordinates: [49.133290, 6.154370]
                },
                {
                    id: 3,
                    imageUrl: 'https://img.icons8.com/doodle/48/000000/croissant--v1.png',
                    coordinates: [49.102160, 6.158850]
                },
                {
                    id: 4,
                    imageUrl: 'https://img.icons8.com/doodle/48/000000/the-toast--v2.png',
                    coordinates: [49.136010, 6.199630]
                },
                {
                    id: 5,
                    imageUrl: 'https://img.icons8.com/doodle/48/000000/hamburger.png',
                    coordinates: [45.413, -75.700]
                },
            ],
            r_circles: [{
                id: 1,
                coordinates: [45.413, -75.700],
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius: 500
            }]
        }
    },
    methods: {
        zoomUpdated(zoom) {
            this.zoom = zoom;
            console.log(this.markers)
        },
        centerUpdated(center) {
            this.center = center;
        }
    }
}
</script>

<style>
.map {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow: hidden
}
</style>
