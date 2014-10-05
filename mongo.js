var mongoose = require("mongoose");

mongoose.connect('mongodb://localhost/heroin_lab');

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));

db.once('open', function(){
  console.log("success bitches");

  var UserSchema = mongoose.Schema({
    username: String,
    passwordHash: String,
    created: {type: Date, default: Date.now}
  });

  var ItemSchema = mongoose.Schema({
    name: String,
    description: String,
    created: {type: Date, default: Date.now},
    type: String,
    price: Number
  });


  var SpellSchema = mongoose.Schema({
    name: String,
    sourcebook: String,
    sourcePage: Number
  });

  var SkillSchema = mongoose.Schema({
    name: String,
    description: String,
    keyAttribute: String,
    trainedOnly: Boolean,
    tryAgain: Boolean,
    sourcebook: String,
    sourcePage: Number
  });

  var SkillLevelSchema = mongoose.Schema({
    skill: mongoose.Schema.Types.ObjectId,
    ranks: Number
  });

  var FeatSchema = mongoose.Schema({
    name: String,
    sourcebook: String,
    sourcePage: Number,
    skillBenefits: [mongoose.Schema.Types.ObjectId]

  });

  var ClassSchema = mongoose.Schema({
    name: String,
    description: String,
    hitDie: String,
    classSkills: [mongoose.Schema.Types.ObjectId],
    sourcebook: String,
    sourcePage: Number
  });

  var ClassLevelSchema = mongoose.Schema({
    class: mongoose.Schema.Types.ObjectId,
    level: Number
  });

  var CharacterSchema = mongoose.Schema({
    name: String,
    classeLevels : [mongoose.Schema.Types.ObjectId]
  });


  var User = mongoose.model('User', UserSchema);
  var Item = mongoose.model('Item', ItemSchema);
  var Spell = mongoose.model('Spell', SpellSchema);
  var Feat = mongoose.model('Feat', FeatSchema);
  var Skill = mongoose.model('Skill', SkillSchema);
  var SkillLevel = mongoose.model('SkillLevel', SkillLevelSchema);
  var ClassLevel = mongoose.model('ClassLevel', ClassLevelSchema);
  var Class = mongoose.model('Class', ClassSchema);
  var Character = mongoose.model('Character', CharacterSchema);


});