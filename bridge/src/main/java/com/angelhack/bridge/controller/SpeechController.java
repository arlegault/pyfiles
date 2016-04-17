package com.angelhack.bridge.controller;

import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.amazonaws.auth.ClasspathPropertiesFileCredentialsProvider;
import com.ivona.services.tts.IvonaSpeechCloudClient;
import com.ivona.services.tts.model.CreateSpeechRequest;
import com.ivona.services.tts.model.CreateSpeechResult;
import com.ivona.services.tts.model.Input;
import com.ivona.services.tts.model.Voice;

/**
 * Class that generates sample synthesis and retrieves audio stream.
 */
@RestController
@RequestMapping("/api/speech")
public class SpeechController {

	private static IvonaSpeechCloudClient speechCloud;

	static {
		init();
	}

	@RequestMapping(value = "/{text}", method = RequestMethod.GET)
	public String textToSpeech(@PathVariable("text") String text) {
		try {

			convertToSpeech(text);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return "Done -> " + text;
	}

	@RequestMapping(method = RequestMethod.GET)
	public void tts(@RequestParam("textToSpeech") String text,
			HttpServletRequest request, HttpServletResponse response) {
		try {
			response.setContentType("audio/mp3");

			convertToSpeech(text, response.getOutputStream());
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private static void init() {
		speechCloud = new IvonaSpeechCloudClient(
				new ClasspathPropertiesFileCredentialsProvider(
						"keys.properties"));
		speechCloud.setEndpoint("https://tts.eu-west-1.ivonacloud.com");
	}

	public static void mainOld(String[] args) throws Exception {
		convertToSpeech("God is great");
	}

	public static void convertToSpeech(String text) throws Exception {

		convertToSpeech(text, new FileOutputStream(
				"/Users/dosapats/speech/speech.mp3"));
	}

	public static void convertToSpeech(String text, OutputStream os)
			throws Exception {
		// init();

		CreateSpeechRequest createSpeechRequest = new CreateSpeechRequest();
		Input input = new Input();
		Voice voice = new Voice();

		voice.setName("Salli");
		input.setData(text);

		createSpeechRequest.setInput(input);
		createSpeechRequest.setVoice(voice);
		InputStream in = null;
		OutputStream outputStream = null;

		try {

			CreateSpeechResult createSpeechResult = speechCloud
					.createSpeech(createSpeechRequest);

			System.out.println("\nSuccess sending request:");
			System.out.println(" content type:\t"
					+ createSpeechResult.getContentType());
			System.out.println(" request id:\t"
					+ createSpeechResult.getTtsRequestId());
			System.out.println(" request chars:\t"
					+ createSpeechResult.getTtsRequestCharacters());
			System.out.println(" request units:\t"
					+ createSpeechResult.getTtsRequestUnits());

			System.out.println("\nStarting to retrieve audio stream:");

			in = createSpeechResult.getBody();
			outputStream = os;
			byte[] buffer = new byte[2 * 1024];
			int readBytes;

			while ((readBytes = in.read(buffer)) > 0) {
				// In the example we are only printing the bytes counter,
				// In real-life scenario we would operate on the buffer
				System.out.println(" received bytes: " + readBytes);
				outputStream.write(buffer, 0, readBytes);
			}

			// System.out.println("\nFile saved: " + outputFileName);

		} finally {
			if (in != null) {
				in.close();
			}
			if (outputStream != null) {
				outputStream.close();
			}
		}
	}
}