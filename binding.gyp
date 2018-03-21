{
	"targets": [
	{
		"target_name": "Speex",
		"defines": ["HAVE_CONFIG_H"],
		"sources": [
			"src/Speex.cc", "src/SpeexDecoder.cc", "src/SpeexEncoder.cc", "src/slots.c", "src/util.cc",
			"src/libspeex/cb_search.c",
			"src/libspeex/exc_10_32_table.c",
			"src/libspeex/exc_8_128_table.c",
			"src/libspeex/filters.c",
			"src/libspeex/gain_table.c",
			"src/libspeex/hexc_table.c",
			"src/libspeex/high_lsp_tables.c",
			"src/libspeex/lsp.c",
			"src/libspeex/ltp.c",
			"src/libspeex/speex.c",
			"src/libspeex/stereo.c",
			"src/libspeex/vbr.c",
			"src/libspeex/vq.c",
			"src/libspeex/bits.c",
			"src/libspeex/exc_10_16_table.c",
			"src/libspeex/exc_20_32_table.c",
			"src/libspeex/exc_5_256_table.c",
			"src/libspeex/exc_5_64_table.c",
			"src/libspeex/gain_table_lbr.c",
			"src/libspeex/hexc_10_32_table.c",
			"src/libspeex/lpc.c",
			"src/libspeex/lsp_tables_nb.c",
			"src/libspeex/modes.c",
			"src/libspeex/modes_wb.c",
			"src/libspeex/nb_celp.c",
			"src/libspeex/quant_lsp.c",
			"src/libspeex/sb_celp.c",
			"src/libspeex/speex_callbacks.c",
			"src/libspeex/speex_header.c",
			"src/libspeex/window.c",
			"src/libspeex/preprocess.c",
			"src/libspeex/jitter.c",
			"src/libspeex/mdf.c",
			"src/libspeex/fftwrap.c",
			"src/libspeex/filterbank.c",
			"src/libspeex/resample.c",
			"src/libspeex/buffer.c",
			"src/libspeex/scal.c",
			"src/libspeex/kiss_fft.c",
			"src/libspeex/kiss_fftr.c",
		],
		"include_dirs": [
			'src',
			'src/include',
		]
	}
	]
}
