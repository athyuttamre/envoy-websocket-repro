# envoy-repro

## Instructions

1. Run the websockets server:

```
pip install websockets
python3 ws.py
```

2. Run the authz server:

```
python3 authz.py
```

3. Run envoy:

```
envoy -c envoy.yaml --base-id 1
```

4. Test a websocket connection:

```
npm install -g wscat
wscat -c ws://localhost:8000/
```

Observe that envoy receives the request, forwards to auth server, which returns a 401, and envoy segfaults with `No status in headers`.

```
...
[2025-02-14 21:15:13.992][189040][info][main] [source/server/server.cc:978] starting main dispatch loop
[2025-02-14 21:19:21.987][189105][error][envoy_bug] [source/common/http/utility.cc:612] envoy bug failure: false. Details: No status in headers
[2025-02-14 21:19:21.987][189105][error][envoy_bug] [./source/common/common/assert.h:38] stacktrace for envoy bug
[2025-02-14 21:19:21.989][189105][error][envoy_bug] [./source/common/common/assert.h:43] #0 Envoy::Http::AsyncRequestSharedImpl::onHeaders() [0x102fb68f8]
[2025-02-14 21:19:21.990][189105][error][envoy_bug] [./source/common/common/assert.h:43] #1 Envoy::Http::AsyncStreamImpl::encodeHeaders() [0x102fb4bd0]
[2025-02-14 21:19:21.990][189105][error][envoy_bug] [./source/common/common/assert.h:43] #2 Envoy::Http::Utility::encodeLocalReply() [0x103424c51]
[2025-02-14 21:19:21.991][189105][error][envoy_bug] [./source/common/common/assert.h:43] #3 Envoy::Http::Utility::sendLocalReply() [0x103424dd3]
[2025-02-14 21:19:21.991][189105][error][envoy_bug] [./source/common/common/assert.h:43] #4 Envoy::Http::AsyncStreamImpl::sendLocalReply() [0x102fb75c6]
[2025-02-14 21:19:21.992][189105][error][envoy_bug] [./source/common/common/assert.h:43] #5 Envoy::Router::UpstreamFilterManager::sendLocalReply() [0x103182006]
[2025-02-14 21:19:21.992][189105][error][envoy_bug] [./source/common/common/assert.h:43] #6 Envoy::Http::ActiveStreamFilterBase::sendLocalReply() [0x1031972ce]
[2025-02-14 21:19:21.992][189105][error][envoy_bug] [./source/common/common/assert.h:43] #7 Envoy::Http::ActiveStreamDecoderFilter::sendLocalReply() [0x10319ba5a]
[2025-02-14 21:19:21.993][189105][error][envoy_bug] [./source/common/common/assert.h:43] #8 Envoy::Router::UpstreamCodecFilter::CodecBridge::decodeHeaders() [0x103184cf8]
[2025-02-14 21:19:21.993][189105][error][envoy_bug] [./source/common/common/assert.h:43] #9 Envoy::Http::Http1::ActiveClient::StreamWrapper::decodeHeaders() [0x102eee1f7]
[2025-02-14 21:19:21.993][189105][error][envoy_bug] [./source/common/common/assert.h:43] #10 Envoy::Http::CodecClient::ActiveRequest::decodeHeaders() [0x102f9ebac]
[2025-02-14 21:19:21.993][189105][error][envoy_bug] [./source/common/common/assert.h:43] #11 Envoy::Http::Http1::ClientConnectionImpl::onMessageCompleteBase() [0x103108098]
[2025-02-14 21:19:21.995][189105][error][envoy_bug] [./source/common/common/assert.h:43] #12 Envoy::Http::Http1::ConnectionImpl::onMessageCompleteImpl() [0x1031010d3]
[2025-02-14 21:19:21.995][189105][error][envoy_bug] [./source/common/common/assert.h:43] #13 Envoy::Http::Http1::ConnectionImpl::onMessageComplete() [0x103100a88]
[2025-02-14 21:19:21.995][189105][error][envoy_bug] [./source/common/common/assert.h:43] #14 Envoy::Http::Http1::BalsaParser::MessageDone() [0x10310ea6f]
[2025-02-14 21:19:21.996][189105][error][envoy_bug] [./source/common/common/assert.h:43] #15 quiche::BalsaFrame::ProcessHeaders() [0x103112169]
[2025-02-14 21:19:21.996][189105][error][envoy_bug] [source/common/http/utility.cc:612] envoy bug failure: false. Details: No status in headers
[2025-02-14 21:19:21.996][189105][error][envoy_bug] [./source/common/common/assert.h:38] stacktrace for envoy bug
[2025-02-14 21:19:21.996][189105][error][envoy_bug] [./source/common/common/assert.h:43] #0 Envoy::Extensions::Filters::Common::ExtAuthz::RawHttpClientImpl::onBeforeFinalizeUpstreamSpan() [0x1005c6fef]
[2025-02-14 21:19:21.996][189105][error][envoy_bug] [./source/common/common/assert.h:43] #1 Envoy::Http::AsyncRequestSharedImpl::onComplete() [0x102fb67ae]
[2025-02-14 21:19:21.997][189105][error][envoy_bug] [./source/common/common/assert.h:43] #2 Envoy::Http::AsyncStreamImpl::encodeHeaders() [0x102fb4bfd]
[2025-02-14 21:19:21.998][189105][error][envoy_bug] [./source/common/common/assert.h:43] #3 Envoy::Http::Utility::encodeLocalReply() [0x103424c51]
[2025-02-14 21:19:21.998][189105][error][envoy_bug] [./source/common/common/assert.h:43] #4 Envoy::Http::Utility::sendLocalReply() [0x103424dd3]
[2025-02-14 21:19:21.999][189105][error][envoy_bug] [./source/common/common/assert.h:43] #5 Envoy::Http::AsyncStreamImpl::sendLocalReply() [0x102fb75c6]
[2025-02-14 21:19:22.000][189105][error][envoy_bug] [./source/common/common/assert.h:43] #6 Envoy::Router::UpstreamFilterManager::sendLocalReply() [0x103182006]
[2025-02-14 21:19:22.000][189105][error][envoy_bug] [./source/common/common/assert.h:43] #7 Envoy::Http::ActiveStreamFilterBase::sendLocalReply() [0x1031972ce]
[2025-02-14 21:19:22.001][189105][error][envoy_bug] [./source/common/common/assert.h:43] #8 Envoy::Http::ActiveStreamDecoderFilter::sendLocalReply() [0x10319ba5a]
[2025-02-14 21:19:22.001][189105][error][envoy_bug] [./source/common/common/assert.h:43] #9 Envoy::Router::UpstreamCodecFilter::CodecBridge::decodeHeaders() [0x103184cf8]
[2025-02-14 21:19:22.002][189105][error][envoy_bug] [./source/common/common/assert.h:43] #10 Envoy::Http::Http1::ActiveClient::StreamWrapper::decodeHeaders() [0x102eee1f7]
[2025-02-14 21:19:22.002][189105][error][envoy_bug] [./source/common/common/assert.h:43] #11 Envoy::Http::CodecClient::ActiveRequest::decodeHeaders() [0x102f9ebac]
[2025-02-14 21:19:22.003][189105][error][envoy_bug] [./source/common/common/assert.h:43] #12 Envoy::Http::Http1::ClientConnectionImpl::onMessageCompleteBase() [0x103108098]
[2025-02-14 21:19:22.003][189105][error][envoy_bug] [./source/common/common/assert.h:43] #13 Envoy::Http::Http1::ConnectionImpl::onMessageCompleteImpl() [0x1031010d3]
[2025-02-14 21:19:22.005][189105][error][envoy_bug] [./source/common/common/assert.h:43] #14 Envoy::Http::Http1::ConnectionImpl::onMessageComplete() [0x103100a88]
[2025-02-14 21:19:22.005][189105][error][envoy_bug] [./source/common/common/assert.h:43] #15 Envoy::Http::Http1::BalsaParser::MessageDone() [0x10310ea6f]
[2025-02-14 21:19:22.007][189105][critical][backtrace] [./source/server/backtrace.h:127] Caught Segmentation fault: 11, suspect faulting address 0xffffffffffffffc0
[2025-02-14 21:19:22.007][189105][critical][backtrace] [./source/server/backtrace.h:111] Backtrace (use tools/stack_decode.py to get line numbers):
[2025-02-14 21:19:22.007][189105][critical][backtrace] [./source/server/backtrace.h:112] Envoy version: 7b8baff1758f0a584dcc3cb657b5032000bcb3d7/1.31.0/Distribution/RELEASE/BoringSSL
[2025-02-14 21:19:22.007][189105][critical][backtrace] [./source/server/backtrace.h:119] #0: _sigtramp [0x7ff80b7aee1d]
[2025-02-14 21:19:22.007][189105][critical][backtrace] [./source/server/backtrace.h:119] #1: 0x0 [0x11a920009]
[2025-02-14 21:19:22.008][189105][critical][backtrace] [./source/server/backtrace.h:119] #2: Envoy::Extensions::Upstreams::Http::Http::HttpUpstream::resetStream() [0x10315b650]
[2025-02-14 21:19:22.008][189105][critical][backtrace] [./source/server/backtrace.h:119] #3: Envoy::Router::UpstreamRequest::resetStream() [0x10317d8fa]
[2025-02-14 21:19:22.008][189105][critical][backtrace] [./source/server/backtrace.h:119] #4: Envoy::Router::Filter::resetAll() [0x10316a0ad]
[2025-02-14 21:19:22.009][189105][critical][backtrace] [./source/server/backtrace.h:119] #5: Envoy::Router::Filter::onDestroy() [0x103169eb3]
[2025-02-14 21:19:22.009][189105][critical][backtrace] [./source/server/backtrace.h:119] #6: Envoy::Http::AsyncStreamImpl::~AsyncStreamImpl() [0x102fb5f03]
[2025-02-14 21:19:22.009][189105][critical][backtrace] [./source/server/backtrace.h:119] #7: Envoy::Http::AsyncRequestImpl::~AsyncRequestImpl() [0x102fb92c6]
[2025-02-14 21:19:22.010][189105][critical][backtrace] [./source/server/backtrace.h:119] #8: Envoy::Event::DispatcherImpl::clearDeferredDeleteList() [0x103305ce2]
[2025-02-14 21:19:22.010][189105][critical][backtrace] [./source/server/backtrace.h:119] #9: event_process_active_single_queue [0x1035b55c9]
[2025-02-14 21:19:22.010][189105][critical][backtrace] [./source/server/backtrace.h:119] #10: event_base_loop [0x1035b2491]
[2025-02-14 21:19:22.011][189105][critical][backtrace] [./source/server/backtrace.h:119] #11: Envoy::Server::WorkerImpl::threadRoutine() [0x102aaa7e5]
[2025-02-14 21:19:22.011][189105][critical][backtrace] [./source/server/backtrace.h:119] #12: Envoy::Thread::PosixThreadFactory::createPthread()::$_1::__invoke() [0x103672dc3]
[2025-02-14 21:19:22.011][189105][critical][backtrace] [./source/server/backtrace.h:119] #13: _pthread_start [0x7ff80b778253]
[2025-02-14 21:19:22.011][189105][critical][backtrace] [./source/server/backtrace.h:119] #14: thread_start [0x7ff80b773bef]
```
