<template>
<div id="admin">
    <v-toolbar color="cyan" dark>
        <v-toolbar-title>Authentication and Authorization</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
        </v-btn>
    </v-toolbar>
    <v-form v-model="valid">
        <v-container>
            <v-select :items="userNames" label="Users" v-model="selected" dense outlined></v-select>
            <v-row>
                <v-col cols="10" md="4">
                    <v-text-field v-model="first" :rules="nameRules" label="First name" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="last" :rules="nameRules" label="Last name" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="is_active" :rules="activeRules" label="Is Active?" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="is_staff" :rules="staffRules" label="Is Admin?" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="last_login" :rules="loginRules" label="Last Login" required></v-text-field>
                </v-col>
            </v-row>
            <v-btn :disabled="true" color="success" class="mr-4" @click="create">
                Create
            </v-btn>

            <v-btn :disabled="true" color="warning" class="mr-4" @click="update">
                Update
            </v-btn>

            <v-btn :disabled="true" color="error" class="mr-4" @click="del">
                Delete
            </v-btn>

            <v-btn color="info" @click="refresh">
                Refresh
            </v-btn>
        </v-container>
    </v-form>
</div>
</template>

<script>
import axios from "axios";
import moment from 'moment';
import Globals from "../Globals";

export default {
    data() {
        return {
            users: [],
            userNames: [],
            selected: '',
            prefix: '',
            first: '',
            last: '',
            email: '',
            is_active: '',
            is_staff: '',
            last_login: ''
        }
    },
    computed: {
        filteredUsers() {
            return this.users.filter((n) =>
                n.toLowerCase().startsWith(this.prefix.toLowerCase())
            )
        }
    },
    watch: {
        selected(userName) {
            console.log(userName)
            let user = this.users.filter(x => x.username === userName)
            this.first = user[0].first_name
            this.last = user[0].last_name
            this.email = user[0].email
            this.is_active = user[0].is_active
            this.is_staff = user[0].is_staff
            this.last_login = user[0].last_login
        }
    },
    methods: {

        async refresh() {
            console.log("refresh user data...")
            this.users = []
            this.userNames = []

            await axios.get(Globals.API_URL + "warchest/viewusers")
                .then((response) => {
                    this.$userData = response.data;
                    const jsonStr = JSON.stringify(this.$userData)
                    const jsObj = JSON.parse(jsonStr);
                    this.users = jsObj

                    for (let i = 0; i < jsObj.length; i++) {
                        this.userNames.push(jsObj[i]['username'])
                    }
                    console.log('---users:' , this.users)
                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                    this.errorMsg = error.message
                })
        },

        create() {
            if (this.hasValidInput()) {
                const userInfo = `${this.last}, ${this.first}, ${this.email}, ${this.role}`
                if (!this.users.includes(userInfo)) {
                    this.users.push(userInfo)
                    this.first = this.last = this.email = this.role = ''
                }
            }
        },
        update() {
            if (this.hasValidInput() && this.selected) {
                const i = this.users.indexOf(this.selected)
                this.users[i] = this.selected = `${this.last}, ${this.first}, ${this.email}, ${this.role}`
            }
        },
        del() {
            if (this.selected) {
                const i = this.users.indexOf(this.selected)
                this.users.splice(i, 1)
                this.selected = this.first = this.last = this.email = this.role = ''
            }
        },
        hasValidInput() {
            return this.first.trim() && this.last.trim() && this.email.trim() && this.role
        }
    }
}
</script>