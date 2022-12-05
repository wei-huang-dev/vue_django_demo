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
            <v-select :items="filteredUsers" label="Users" v-model="selected" dense outlined></v-select>
            <v-row>
                <v-col cols="10" md="4">
                    <v-text-field v-model="first" :rules="nameRules" :counter="10" label="First name" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="last" :rules="nameRules" :counter="10" label="Last name" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                </v-col>

                <v-col cols="10" md="4">
                    <v-text-field v-model="role" :rules="roleRules" label="Role" required></v-text-field>
                </v-col>
            </v-row>
            <v-btn :disabled="!valid" color="success" class="mr-4" @click="create">
                Create
            </v-btn>

            <v-btn color="warning" class="mr-4" @click="update">
                Update
            </v-btn>

            <v-btn color="error" @click="del">
                Delete
            </v-btn>
        </v-container>
    </v-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            users: ['Emil, Hans, eh@abc.com, Admin', 'Mustermann, Max, mm@abc.com, tester', 'Tisch, Roman, tr@abc.com, dba'],
            names: [],
            selected: '',
            prefix: '',
            first: '',
            last: '',
            email: '',
            role: ''
        }
    },
    computed: {
        filteredUsers() {
            this.names = this.users.map(obj => (obj.slice(0, 12)));
            console.log(this.names);
            return this.users.filter((n) =>
                n.toLowerCase().startsWith(this.prefix.toLowerCase())
            )
        }
    },
    watch: {
        selected(name) {

            [this.last, this.first, this.email, this.role] = name.split(', ')
        }
    },
    methods: {
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