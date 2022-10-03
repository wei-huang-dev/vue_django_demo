<template>
<div class="text-center">
    <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="400">
            <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                    Edit
                </v-btn>
            </template>
            <v-card>
                <v-card-title class="text-h5">
                    Edit Photo
                </v-card-title>
                <v-card-text>Display or select photo to be uploaded.</v-card-text>
                <v-row>
                    <v-col class="ml-10">
                        <v-combobox v-model="title" :items="titles" label="Title" outlined dense></v-combobox>
                    </v-col>
                    <v-col>
                        <v-combobox v-model="date" :items="dates" label="Date" outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-btn @click="showPhoto">Show</v-btn>
                    </v-col>
                </v-row>
                <v-row align="center" justify="center">
                    <v-simple-table height="100%" width="100%">
                        <template v-slot:default>
                            <thead>
                                <tr>
                                    <th class="text-left" v-for="(item, index) in fields">
                                        Field {{ index+1 }}
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td v-for="(item, index) in fields">
                                        {{item}}
                                    </td>
                                </tr>
                            </tbody>
                        </template>
                    </v-simple-table>
                </v-row>
                <v-divider></v-divider>
                <v-row align="center" justify="center">
                    <v-img :aspect-ratio="4/3" :width=120 :src=PHOTO_URL+photoFileName></v-img>
                    <input class="m-2" type="file" @change="photoUpload">
                </v-row>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="green darken-1" text @click="updateClick()">
                        Upload
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</div>
</template>

<script>
import axios from "axios";
import CONSTANTS from "../Constants";

export default {
    data() {
        return {
            PHOTO_URL: CONSTANTS.PHOTO_URL,
            dialog: false,
            photoFileName: "sample.png",
            fieldTables: [],
            id: null,
            title: [],
            titles: [
                'ABC',
                'DEF',
                'GIJ',
                'KLM',
            ],
            date: [],
            dates: [
                '2022-08-17',
                '2022-08-18',
            ],
            fields: [],

        }
    },

    methods: {

        photoUpload(event) {
            let formData = new FormData();
            formData.append('file', event.target.files[0]);
            axios.post(
                    this.$API_URL + "warchest/savefile",
                    formData)
                .then((response) => {
                    this.photoFileName = response.data;
                    console.log("photoUpload :" + this.photoFileName);
                });

        },

        updateClick() {
            axios.put(this.$API_URL + "warchest", {
                    Id: this.id,
                    Title: this.title,
                    Field1: this.fields[0],
                    Field2: this.fields[1],
                    Field3: this.fields[2],
                    Field4: this.fields[3],
                    Field5: this.fields[4],
                    Date: this.date,
                    photoFileName: this.photoFileName
                })
                .then((response) => {
                    alert(response.data);
                });
        },

        showPhoto() {
            // should get data from fieldTable component
            this.$http.get(this.$API_URL + "warchest")
                .then((response) => {
                    this.$warchestData = response.data;
                    const jsonStr = JSON.stringify(this.$warchestData)
                    const jsObj = JSON.parse(jsonStr);
                    this.fields = [];
                    for (let i = 0; i < jsObj.length; i++) {
                        if ((jsObj[i]['Title'] === this.title) && (jsObj[i]['Date'] === this.date)) {
                            this.photoFileName = jsObj[i]['photoFileName'];
                            this.id = jsObj[i]['Id'];
                            this.date = jsObj[i]['Date'];
                            this.fields.push(jsObj[i]['Field1'])
                            this.fields.push(jsObj[i]['Field2'])
                            this.fields.push(jsObj[i]['Field3'])
                            this.fields.push(jsObj[i]['Field4'])
                            this.fields.push(jsObj[i]['Field5'])
                            console.log(this.id + "--photoFileName:   " + this.photoFileName);
                            break;
                        }
                    }
                });
        },
    },
    components: {
        'dropdownButton': require('@/components/DropdownButton.vue').default,
    }
}
</script>
