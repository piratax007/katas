import { it, describe } from "mocha";
import { expect } from "chai";
import { functions } from "./code";

describe("test suit description", () => {
    describe("test description"), () => {
	it("dummy test", () => {
            let variable = 3;
            expect(variable).to.equal(2);
	});
    }
});
