
module.exports = {

	 hex2base64: (x) => {
		return Buffer.from(x,'hex').toString('base64')
	}

}
