To run this demo app 
1. Have [node.js](https://nodejs.org/en/download) installed
2. Install dependencies using 

```shell
npm install
```

You may need to uninstall `pgx-ka` using

```shell
npm uninstall pgx-ka
```

and then install it from a local place or published version if any, using

```shell
npm install /home/path/to/knowledge-assembly-exploration-1/pgx-ka
```

If you are installing pgx-ka from a local place, make sure all its dependencies are installed there by running `npm install` in the root of that local place.

3. Then run the application using the following command
```shell
npx vite   
```

For production first build the app and then copy the information pages to the demo folder using
```shell
npx vite build 
cp ../../pgx-ka/index.html dist/pgx_ka_info_page.html
cp ../../collection/CPIC_Phenotype_CYP2D6/index.html dist/CPIC_Phenotype_CYP2D6.html
cp ../../collection/CPIC_Phenotype_CYP2C9/index.html dist/CPIC_Phenotype_CYP2C9.html
cp ../../collection/CPIC_Phenotype_CYP2C19/index.html dist/CPIC_Phenotype_CYP2C19.html
cp ../../collection/CPIC_Phenotype_CYP3A5/index.html dist/CPIC_Phenotype_CYP3A5.html
cp ../../collection/CPIC_Phenotype_SLCO1B1/index.html dist/CPIC_Phenotype_SLCO1B1.html
cp ../../collection/CPIC_Phenotype_TPMT/index.html dist/CPIC_Phenotype_TPMT.html
cp ../../collection/CPIC_Phenotype_UGT1A1/index.html dist/CPIC_Phenotype_UGT1A1.html
cp ../../collection/CPICRec_codeine_CYP2D6/index.html dist/CPICRec_Codeine_CYP2D6.html
cp ../../collection/CPICRec_abacavir_HLA-B/index.html dist/CPIC_abacavir.html
cp ../../collection/CPICRec_allopurinol_HLA-B/index.html dist/CPIC_allopurinol.html
cp ../../collection/CPICRec_amitriptyline_CYP2C19_CYP2D6/index.html dist/CPIC_amitriptyline.html
cp ../../collection/CPICRec_atazanavir_UGT1A1/index.html dist/CPIC_atazanavir.html
cp ../../collection/CPICRec_azathioprine_TPMT/index.html dist/CPIC_azathioprine.html
cp ../../collection/CPICRec_carbamazepine_HLA-A_HLA-B/index.html dist/CPIC_carbamazepine.html
cp ../../collection/CPICRec_citalopram_CYP2C19/index.html dist/CPIC_citalopram.html
cp ../../collection/CPICRec_clomipramine_CYP2C19_CYP2D6/index.html dist/CPIC_clomipramine.html
cp ../../collection/CPICRec_clopidogrel_CYP2C19/index.html dist/CPIC_clopidogrel.html
cp ../../collection/CPICRec_codeine_CYP2D6/index.html dist/CPIC_codeine.html
cp ../../collection/CPICRec_desipramine_CYP2C19_CYP2D6/index.html dist/CPIC_desipramine.html
cp ../../collection/CPICRec_doxepin_CYP2C19_CYP2D6/index.html dist/CPIC_doxepin.html
cp ../../collection/CPICRec_escitalopram_CYP2C19/index.html dist/CPIC_escitalopram.html
cp ../../collection/CPICRec_fluvoxamine_CYP2D6/index.html dist/CPIC_fluvoxamine.html
cp ../../collection/CPICRec_imipramine_CYP2C19_CYP2D6/index.html dist/CPIC_imipramine.html
cp ../../collection/CPICRec_mercaptopurine_TPMT/index.html dist/CPIC_mercaptopurine.html
cp ../../collection/CPICRec_nortripyline_CYP2C19_CYP2D6/index.html dist/CPIC_nortripyline.html
cp ../../collection/CPICRec_ondansetron_CYP2D6/index.html dist/CPIC_ondansetron.html
cp ../../collection/CPICRec_oxcarbazepine_HLA-B/index.html dist/CPIC_oxcarbazepine.html
cp ../../collection/CPICRec_paroxetine_CYP2D6/index.html dist/CPIC_paroxetine.html
cp ../../collection/CPICRec_phenytoin_CYP2C9_HLA-B/index.html dist/CPIC_phenytoin.html
cp ../../collection/CPICRec_sertraline_CYP2C19/index.html dist/CPIC_sertraline.html
cp ../../collection/CPICRec_simvastatin_SLCO1B1/index.html dist/CPIC_simvastatin.html
cp ../../collection/CPICRec_tacrolimus_CYP3A5/index.html dist/CPIC_tacrolimus.html
cp ../../collection/CPICRec_thioguanine_TPMT/index.html dist/CPIC_thioguanine.html
cp ../../collection/CPICRec_tramadol_CYP2D6/index.html dist/CPIC_tramadol.html
cp ../../collection/CPICRec_trimipramine_CYP2C19_CYP2D6/index.html dist/CPIC_trimipramine.html
cp ../../collection/CPICRec_tropisetron_CYP2D6/index.html dist/CPIC_tropisetron.html
cp ../../collection/CPICRec_voriconazole_CYP2C19/index.html dist/CPIC_voriconazole.html
cp ../../collection/DPWGRec_amitriptyline_CYP2C19/index.html dist/DPWG_amitriptyline.html
cp ../../collection/DPWGRec_clomipramine_CYP2C19/index.html dist/DPWG_clomipramine.html
cp ../../collection/DPWGRec_escitalopram_CYP2C19/index.html dist/DPWG_escitalopram.html
```

To run a built version in dev environment use serve
```shell
npm install -g serve
serve dist
```

To deploy the build on GitHub pages (push the dist folder to gh-pages branch) use the following command:
```shell
npm run deploy
```
