# import here so fbs compiles into application
import uvicorn.protocols.http.auto
#import uvicorn.protocols.http.h11_impl
#import uvicorn.protocols.http.httptools_impl

import uvicorn.protocols.websockets.auto
#import uvicorn.protocols.websockets.websockets_impl
#import uvicorn.protocols.websockets.wsproto_impl

import uvicorn.loops.auto
#import uvicorn.loops.asyncio
#import uvicorn.loops.uvloop
