const {expect} = require('chai');
const {Shop, Item} = require('../src/gilded_rose.js');

describe("The function updateQuality", function() {
    it("with a normal article should decrease quality by one", () => {
        const gildedRose = new Shop([ new Item("normal article", 10, 5) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(9)
        expect(items[0].quality).to.equal(4);
    });

    it("with a normal article that does not have available days, should decrease quality by two", () => {
        const gildedRose = new Shop([ new Item("normal article", 0, 4) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-1)
        expect(items[0].quality).to.equal(2);
    });

    it("with a normal article that has quality 0, should't change the quality without care the sellIn value", () => {
        let gildedRose = new Shop([ new Item("normal article", 12, 0) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(11)
        expect(items[0].quality).to.equal(0);

        gildedRose = new Shop([ new Item("normal article", 0, 0) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-1)
        expect(items[0].quality).to.equal(0);

        gildedRose = new Shop([ new Item("normal article", -10, 0) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-11)
        expect(items[0].quality).to.equal(0);
    });

    it("with 'Aged Brie' that has sellIn greater than zero, shoul increase their quality by one if their quality is lesser than 50", () => {
        let gildedRose = new Shop([ new Item("Aged Brie", 3, 10) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(2)
        expect(items[0].quality).to.equal(11);

        gildedRose = new Shop([ new Item("Aged Brie", 1, 0) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(0)
        expect(items[0].quality).to.equal(1);

        gildedRose = new Shop([ new Item("Aged Brie", 5, 50) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(4);
        expect(items[0].quality).to.equal(50);
    });

    it("with 'Aged Brie' that has zero or lesser sellIn propertie, should increase their quality by two if their quality is lesser than 50", () => {
        let gildedRose = new Shop([ new Item("Aged Brie", 0, 4) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-1)
        expect(items[0].quality).to.equal(6);

        gildedRose = new Shop([ new Item("Aged Brie", -2, 6) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-3)
        expect(items[0].quality).to.equal(8);

        gildedRose = new Shop([ new Item("Aged Brie", -3, 0) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-4)
        expect(items[0].quality).to.equal(2);

        gildedRose = new Shop([ new Item("Aged Brie", -1, 50) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-2)
        expect(items[0].quality).to.equal(50);
    });

    it("with 'Aged Brie' that has 50 quality and 0 sellIn, should not be increased the quality value", () => {
        const gildedRose = new Shop([ new Item("Aged Brie", 0, 50) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-1)
        expect(items[0].quality).to.equal(50);
    });

    it("with a sulfuras article, should't change their sellIn value", () => {
        /*const gildedRose = new Shop([ new Item("Sulfuras", 0, 50) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(0)*/

        let gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", 10, 30) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(10);

        gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", 0, 9) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(0);

        gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", -3, 7) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-3);
    })

    it("with a sulfuras article, should't change their quality value", () => {
        /*const gildedRose = new Shop([ new Item("Sulfuras", 0, 50) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].quality).to.equal(0)*/

        let gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", 10, 30) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].quality).to.equal(30);

        gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", 0, 0) ]);
        items = gildedRose.updateQuality();
        expect(items[0].quality).to.equal(0);

        gildedRose = new Shop([ new Item("Sulfuras, Hand of Ragnaros", -1, -1) ]);
        items = gildedRose.updateQuality();
        expect(items[0].quality).to.equal(-1);
    });

    it("with a new Backstage entry, should increase their quality by one, if more than 10 days left", () => {
        /*const gildedRose = new Shop([ new Item("Backstage passes to a Mastropiero concert", 15, 30) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(14)
        expect(items[0].quality).to.equal(31);*/

        const gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", 15, 30) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(14)
        expect(items[0].quality).to.equal(31);
    });

    it("with a new Backstage entre, should increase their quality by 2, if 10 days or less left", () => {
        /*const gildedRose = new Shop([ new Item("Backstage passes to a Mastropiero concert", 10, 30) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(9)
        expect(items[0].quality).to.equal(32);*/
        
        let gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", 10, 30) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(9)
        expect(items[0].quality).to.equal(32);

        gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", 8, 30) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(7)
        expect(items[0].quality).to.equal(32);
    });

    it("with a new Backstage entre, should increase their quality by 3, if 5 days or less left", () => {
        /*const gildedRose = new Shop([ new Item("Backstage passes to a Mastropiero concert", 5, 20) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(9)
        expect(items[0].quality).to.equal(32);*/
        
        let gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", 5, 20) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(4)
        expect(items[0].quality).to.equal(23);

        gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", 3, 20) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(2)
        expect(items[0].quality).to.equal(23);
    });

    it("with a new Backstage entre, should their quality shoul change to 0, if the sellIn pass", () => {
        /*const gildedRose = new Shop([ new Item("Backstage passes to a Mastropiero concert", -1, 20) ]);
        const items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-2)
        expect(items[0].quality).to.equal(0);*/
        
        let gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", -1, 20) ]);
        let items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-2)
        expect(items[0].quality).to.equal(0);

        gildedRose = new Shop([ new Item("Backstage passes to a TAFKAL80ETC concert", -2, 50) ]);
        items = gildedRose.updateQuality();
        expect(items[0].sellIn).to.equal(-3)
        expect(items[0].quality).to.equal(0);
    });
});
