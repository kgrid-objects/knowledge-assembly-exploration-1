# PGx-KA All-recommendation Service Documentation

## Library Service
Library service could be used both on client side or server side. This service will load the knwoledge objects at build time.
### Client Side at Build time
To import and use library service of pgx-ka on the client side js files that execute on the beroswer without any need for server side processing install the pgx-ka package as a dependency in your node.js app using

```batch
npm install /path/to/pgx-ka
```

In your client side js import the pgx-ka package using

```javascript
import pgx from 'pgx-ka/library-service';


```

then initialize the run the service using

```javascript
let result = await pgx.run({
    "patient": {
        "name": "Hank Hill",
        "id": "1"
    },
    "diplotype": {
      "CYP2C19": "*1/*11",
      "CYP2C9": "",
      "CYP2D6": "*3/*3",
      "CYP3A5": "",
      "HLA-B": "*1/*1",
      "SLCO1B1": "",
      "TPMT": "",
      "UGT1A1": "*1/*1"
    },
    "prescriptions": "atazanavir codeine abacavir"
  }
);
```

Note that your client side js file needs to be imported with type="module" like the following example
```html
<script type="module" src="static/js/cpic.js"> </script>
```

Then add a `vite.config.js` as the build config for vite with the following content
```javascript
export default {
  root: '.',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: 'index.html'
    }
  }
}
```  

Then run the application using the following command
```shell
npx vite   
```

For production, build the app using
```shell
npx vite build 
```

To run a built version in dev environment use serve
```shell
npm install -g serve
serve dist
```

See the [demo app](/pgx-demos/pgx-demo_library-service_client_side_load/) that uses library service from [pgx-ka](/pgx-ka/) on the client side, for a complete demo example.

### Server Side at Build Time
To use library service on server side, install the pgx-ka package as a dependency in your node.js app using

```batch
npm install /path/to/pgx-ka
```

Then import and use the run method from the library service of the pgx-ka package in your serverside code (node.js) using

```javascript
import pgx from 'pgx-ka/library-service';
const run = pgx.run;
```

Then initialize the package and run the service using

```javascript
let result = await run({
    "patient": {
        "name": "Hank Hill",
        "id": "1"
    },
    "diplotype": {
      "CYP2C19": "*1/*11",
      "CYP2C9": "",
      "CYP2D6": "*3/*3",
      "CYP3A5": "",
      "HLA-B": "*1/*1",
      "SLCO1B1": "",
      "TPMT": "",
      "UGT1A1": "*1/*1"
    },
    "prescriptions": "atazanavir codeine abacavir"
  }
);
```

See the [demo app](/pgx-demos/pgx-demo_library-service_server_side_load/) that uses library service from [pgx-ka](/pgx-ka/) on the server side, for a complete demo example.


## API Service
Run the API service using

```shell
node all-recommendation/api-service.js
```

from the cpic-kb folder and access the api through swagger editor using `http://localhost:3000/api-docs` or send a post request to `http://localhost:3000/run`.

Here is a sample input
```json
{
    "patient": {
        "name": "Hank Hill",
        "id": "1"
    },
    "diplotype": {
      "CYP2C19": "*1/*11",
      "CYP2C9": "",
      "CYP2D6": "*3/*3",
      "CYP3A5": "",
      "HLA-B": "*1/*1",
      "SLCO1B1": "",
      "TPMT": "",
      "UGT1A1": "*1/*1"
    },
    "prescriptions": "atazanavir codeine abacavir"
  }

```

## Plugin Service
Plugin service could be used both on client side or server side. This service will load the knwoledge objects at runtime.
### Client Side at Runtime
To import and use plugin service of pgx-ka on the client side js files that execute on the beroswer without any need for server side processing install the pgx-ka package as a dependency in your node.js app using

```batch
npm install /path/to/pgx-ka
```

To be able to load pgx-ka metadata in the browser of the app, copy it to the public folder by adding the following script to the package.json
```json
  "scripts": {
    "prebuild": "mkdir -p public/pgx-ka && cp node_modules/pgx-ka/metadata.json public/pgx-ka/metadata.json",
    "build": "npm run prebuild && vite build"
  }
```

and running the following command in the shell
```shell
npm run build  
```

In your client side js import the pgx-ka package using

```javascript
import pgx from 'pgx-ka/plugin-service';


```

then initialize the package and run the service using

```javascript
async function initialize() {
  await pgx.initialize();
}


initialize();

let result = await pgx.run({
    "patient": {
        "name": "Hank Hill",
        "id": "1"
    },
    "diplotype": {
      "CYP2C19": "*1/*11",
      "CYP2C9": "",
      "CYP2D6": "*3/*3",
      "CYP3A5": "",
      "HLA-B": "*1/*1",
      "SLCO1B1": "",
      "TPMT": "",
      "UGT1A1": "*1/*1"
    },
    "prescriptions": "atazanavir codeine abacavir"
  }
);
```

Note that your client side js file needs to be imported with type="module" like the following example
```html
<script type="module" src="static/js/cpic.js"> </script>
```

Then add a `vite.config.js` as the build config for vite with the following content
```javascript
export default {
  root: '.',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: 'index.html'
    }
  }
}
```  

Then run the application using the following command
```shell
npx vite   
```

For production, build the app using
```shell
npx vite build 
```

To run a built version in dev environment use serve
```shell
npm install -g serve
serve dist
```

See the [demo app](/pgx-demos/pgx-demo_plugin-service_client_side_load/) that uses plugin service from [pgx-ka](/pgx-ka/) on the client side, for a complete demo example.

### Server Side at Runtime
To use plugin service on server side, install the pgx-ka package as a dependency in your node.js app using

```batch
npm install /path/to/pgx-ka
```

Then import and use the initialize and run methods from plugin service of the pgx-ka package in your serverside code (node.js) using

```javascript
import pgx from 'pgx-ka/plugin-service';
const initialize = pgx.initialize;
const run = pgx.run;
```

Then initialize the package and run the service using

```javascript
await initialize();
let result = await run({
    "patient": {
        "name": "Hank Hill",
        "id": "1"
    },
    "diplotype": {
      "CYP2C19": "*1/*11",
      "CYP2C9": "",
      "CYP2D6": "*3/*3",
      "CYP3A5": "",
      "HLA-B": "*1/*1",
      "SLCO1B1": "",
      "TPMT": "",
      "UGT1A1": "*1/*1"
    },
    "prescriptions": "atazanavir codeine abacavir"
  }
);
```

See the [demo app](/pgx-demos/pgx-demo_plugin-service_server_side_load/) that uses plugin service from [pgx-ka](/pgx-ka/) on the server side, for a complete demo example.
