<template>
<div>
    <br />
    <div>
        <v-data-table :headers="headers" :items="closureAreas" sort-by="id" v-model="selected" @input="drawSelected($event)" show-select class="elevation-1">
            <template v-slot:top>
                <v-toolbar flat>
                    <v-dialog v-model="dialog" max-width="500px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                                New Closure Area
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.name" label="Name"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.country" label="Country"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.latitude" label="Latitude"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.longitude" label="Longitude"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.radius" label="Radius"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="editedItem.start_date" label="Start date"></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="close">
                                    Cancel
                                </v-btn>
                                <v-btn color="blue darken-1" text @click="save">
                                    Save
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <!-- ------------------------------------------------------------------------- -->
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-dialog v-model="dialogFilter" max-width="500px">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                                Filter Closure Areas
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">Filter Closure Areas</span>
                            </v-card-title>

                            <v-card-text>
                                <v-container>
                                    <!-- <v-row>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="queryItem.startDate" label="Start Date"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="queryItem.endDate" label="End Date"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="queryItem.country" label="Country"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field v-model="queryItem.longitude" label="Shape"></v-text-field>
                                        </v-col>
                                    </v-row> -->
                                </v-container>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="closeFilter">
                                    Cancel
                                </v-btn>
                                <v-btn color="blue darken-1" text @click="closeFilter">
                                    Filter
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-divider class="mx-4" inset vertical></v-divider>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" dark class="mb-2" @click="getData">
                        Refresh
                    </v-btn>

                    <v-dialog v-model="dialogDelete" max-width="500px">
                        <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete Area [{{editedItem.id}}]?</v-card-title>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:item.actions="{ item }">
                <v-icon small class="mr-2" @click="editItem(item)">
                    mdi-pencil
                </v-icon>
                <v-icon small @click="deleteItem(item)">
                    mdi-delete
                </v-icon>
            </template>
        </v-data-table>
        <template>
            <v-dialog v-model="errored">
                <p class="error">
                    <center>{{ errorMsg }}</center>
                </p>
            </v-dialog>
        </template>
    </div>

    <div>

        Zoom: level {{ zoom }}
        <!-- <input v-model.number="zoom" type="number"> -->
        &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
        Center : <span> {{ center }} </span><br>
        <hr>

    </div>
    <v-img height="100%" width="100%">
        <l-map ref="map" @ready="onReady()" :zoom.sync="zoom" :options="mapOptions" :center="center" :bounds="bounds" :min-zoom="minZoom" :max-zoom="maxZoom" style="height: 500px; width: 100%">
            <l-control-layers :position="layersPosition" :collapsed="false" :sort-layers="true" />
            <l-tile-layer v-for="tileProvider in tileProviders" :key="tileProvider.name" :name="tileProvider.name" :visible="tileProvider.visible" :url="tileProvider.url" :attribution="tileProvider.attribution" :token="token" layer-type="base" />
            <l-control-zoom :position="zoomPosition" />
            <l-control-attribution :position="attributionPosition" :prefix="attributionPrefix" />
            <l-control-scale :imperial="imperial" />
        </l-map>
    </v-img>
</div>
</template>

<script>
import axios from "axios";
import Globals from "../Globals";
// import * as theEllipse from "../plugins/l.ellipse.js"; // !magic

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

import 'leaflet/dist/leaflet.css'; // needed for full map

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
        url: '/LondonLeMans/OSMPublicTransport/{z}/{x}/{y}.png', // offline
        // url: '/img/mapTiles/{z}/{x}/{y}.png',

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
            closureAreaTables: [],
            closureAreaTable: '',
            selected: [],
            dialog: false,
            dialogFilter: false,
            dialogDelete: false,
            errored: false,
            errorMsg: '',
            headers: [{
                    text: 'ID',
                    align: 'start',
                    sortable: true,
                    value: 'id',
                },
                {
                    text: 'Country',
                    value: 'fk_country_id'
                },
                {
                    text: 'Shape',
                    value: 'fk_shape_id'
                },
                {
                    text: 'Latitude',
                    value: 'latitude'
                },
                {
                    text: 'Longitude',
                    value: 'longitude'
                },
                {
                    text: 'Radius',
                    value: 'radius'
                },
                {
                    text: 'StartDate',
                    value: 'start_date'
                },
                {
                    text: 'Polygon',
                    value: 'polygon'
                },
                {
                    text: 'Actions',
                    value: 'actions',
                    sortable: false
                },
            ],
            closureAreas: [],
            id: null,
            name: '',
            editedIndex: -1,
            editedItem: {
                id: null,
                name: '',
                country: null,
                shape: null,
                latitude: null,
                longitude: null,
                radius: null,
            },
            defaultItem: {
                id: null,
                name: '',
                country: null,
                shape: null,
                latitude: null,
                longitude: null,
                radius: null,
            },
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
            // attributionPrefix: 'Vue2Leaflet',
            // imperial: false,
            Positions: ['topleft', 'topright', 'bottomleft', 'bottomright'],
            tileProviders: tileProviders,
            displayItems: L.featureGroup(),
            ellipse: null,
        };
    },

    computed: {
        formTitle() {
            return this.editedIndex === -1 ? 'New Area' : 'Edit Area'
        },
    },

    watch: {
        dialog(val) {
            val || this.close()
        },
        dialogFilter(val) {
            console.log(val)
            val || this.closeFilter()
        },
        dialogDelete(val) {
            console.log(val)
            val || this.closeDelete()
        }
    },

    created() {
        this.initialize()
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

        onMapClick: function (e) {
            console.log(e.latlng.toString())
        },

        initialize() {
            this.closureAreaTable = 'ClosureAreas'
            this.getData()
        },

        drawSelected(items) {
            if (this.displayItems != null) {
                this.map.removeLayer(this.displayItems)
                this.displayItems = L.featureGroup() // reset
            }

            let centerLat = 0
            let centerLng = 0
            let size = items.length

            items.forEach((item) => {
                if (item.fk_shape_id == 1) { // circle
                    L.circle({
                        'lat': item.latitude,
                        'lng': item.longitude
                    }, {
                        color: 'red',
                        radius: item.radius * 100
                    }).addTo(this.displayItems)

                    centerLat += item.latitude
                    centerLng += item.longitude
                } else { // polygon
                    let polygonAry = JSON.parse(item.polygon)
                    L.polygon(polygonAry, {
                        color: 'blue'
                    }).addTo(this.displayItems)

                    centerLat += polygonAry[0][0]
                    centerLng += polygonAry[0][1]
                }

                this.map.addLayer(this.displayItems)
                this.center = [centerLat / size, centerLng / size]
                this.map.setView(this.center, 8);
            })
        },

        async getData() {
            this.disabled = false
            console.log("Get data from " + this.closureAreaTable)
            this.closureAreas = []

            await axios.get(Globals.API_URL + this.closureAreaTable.toLowerCase())
                .then((response) => {
                    this.closureAreas = response.data
                    console.log(this.closureAreas)
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                    this.errorMsg = error.message
                })
                .finally(() => this.loading = false)
        },

        async postData(newItem) {
            console.log("post " + newItem.name + " to " + this.closureAreaTable)

            await axios.post(Globals.API_URL + this.closureAreaTable.toLowerCase() + "/", {
                    // id: newItem.id,   Current backend creates auto-increment ID (?)
                    name: newItem.name,
                    latitude: newItem.latitude,
                    longitude: newItem.longitude,
                    radius: newItem.radius,
                    country: newItem.country,
                    shape: newItem.shape
                })
                .then((response) => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                    this.errorMsg = error.message
                })
        },

        async putData(editedItem) {
            console.log("put " + editedItem.name + " to " + this.closureAreaTable)

            await axios.put(Globals.API_URL + this.closureAreaTable.toLowerCase() + "/" +
                    editedItem.id + "/", {
                        id: editedItem.id,
                        name: editedItem.name
                    })
                .then((response) => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                    this.errorMsg = error.message
                })
        },

        async deleteData(deletedItem) {
            console.log("Delete " + deletedItem.name + " to " + this.closureAreaTable)

            await axios.delete(Globals.API_URL + this.closureAreaTable.toLowerCase() + "/" +
                    deletedItem.id + "/")
                .then((response) => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error.message)
                    this.errored = true
                    this.errorMsg = error.message
                })
        },

        editItem(item) {
            closeDelete
            this.editedIndex = this.closureAreas.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem(item) {
            this.editedIndex = this.closureAreas.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },

        deleteItemConfirm() {
            // UI test: this.closureAreas.splice(this.editedIndex, 1)
            this.deleteData(this.editedItem)
            this.getData()
            this.closeDelete()
        },

        close() {
            this.dialog = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        closeFilter() {
            this.dialogFilter = false
            this.$nextTick(() => {
                // this.filterItem = Object.assign({}, this.defaultItem)
                // this.filterIndex = -1
            })
        },

        closeDelete() {
            this.dialogDelete = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        save() {
            console.log('save: ' + this.editedItem.name + ' editedIndex: ' + this.editedIndex)

            if (this.editedIndex > -1) {
                this.putData(this.editedItem)
                // UI testing without backend:  Object.assign(this.closureAreas[this.editedIndex], this.editedItem)
            } else {
                this.postData(this.editedItem)
                // check for valid ID...
                // UI testing without backend: this.closureAreas.push(this.editedItem)
            }
            this.getData() // backend verify
            this.close()
        },

    },
};
</script>
