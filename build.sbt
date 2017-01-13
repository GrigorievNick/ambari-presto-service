import com.typesafe.sbt.packager.MappingsHelper._

name := "ambari-presto-service"

version := "0.161"

scalaVersion := "2.12.1"

val metaInfoConfig: String = "presto/metainfo.xml"

lazy val `ambari-presto-service` = project
  .in(file("presto"))
  .enablePlugins(UniversalPlugin)
  .settings(
    topLevelDirectory := Some("PRESTO"),
    mappings in(Universal, packageBin) ++= contentOf("presto"),
    mappings in(Universal, packageBin) += {
      val buildVersion = version.value + "-build-" + sys.env.getOrElse("BUILD_NUMBER", "local")
      val content =
        IO.read(file(metaInfoConfig)).replaceAll("<version>.*</version>", s"<version>$buildVersion</version>")
      val templateFile = file(target.value.getAbsolutePath + "/" + metaInfoConfig)
      IO.write(templateFile, content)
      templateFile
    } -> metaInfoConfig
  )