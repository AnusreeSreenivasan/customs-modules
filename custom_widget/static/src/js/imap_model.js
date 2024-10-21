import { UseService } from "@web/core/utils/hooks"

export class LeafletMapModel {
    constructor(){
        this.orm = UseService("orm")
    }
    async load(){
        const data = this.orm.searhRead("ajs.conact", [],["name"])
        this.records = data

    }
}